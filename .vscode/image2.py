import cv2
import pywt
import numpy as np
from nistrng import *
from nistrng import SP800_22R1A_BATTERY
from nistrng import check_eligibility_all_battery
from nistrng import run_all_battery


# ===== Lấy LL từ DWT =====
def LL_form():
    image = cv2.imread("example.jpg", cv2.IMREAD_GRAYSCALE)
    image = np.float32(image)

    LL, (LH, HL, HH) = pywt.dwt2(image, 'haar')

    LL_norm = (LL - LL.min()) / (LL.max() - LL.min())

    print("Kích thước LL:", LL.shape)

    return LL_norm.flatten()


# ===== Logistic map =====
def logistic_map(N):
    r = 3.99
    x = 0.37
    seq = []

    for i in range(N):
        x = r * x * (1 - x)
        seq.append(x)

    return np.array(seq)


# ===== Chaos mixing =====
def chaos_mixing(seq):
    mixed = (seq + np.roll(seq, 1)) % 1
    return mixed


# ===== Sinh bit dựa trên LL =====
def generate_bits(seq, LL_vec):

    bits = ""

    for i in range(len(seq)):

        x = seq[i]
        LL = LL_vec[i]

        if x < LL / 2:
            bits += "00"

        elif x < LL:
            bits += "01"

        elif x < (LL + 1) / 2:
            bits += "10"

        else:
            bits += "11"

    return bits


# ===== Pipeline =====
LL_vec = LL_form()

seq = logistic_map(len(LL_vec))

# trộn chaotic để giảm correlation
seq_mixed = chaos_mixing(seq)

bit_string = generate_bits(seq_mixed, LL_vec)

print("Tổng bit:", len(bit_string))
print("Ví dụ bit:", bit_string[:200])


# ===== Convert sang numpy =====
bits = np.array([int(b) for b in bit_string])


# ===== NIST TEST =====
print("\n===== NIST TEST =====")

eligible_tests = check_eligibility_all_battery(bits, SP800_22R1A_BATTERY)

results = run_all_battery(bits, eligible_tests)

for result, elapsed in results:

    print(
        result.name,
        "score:", result.score,
        "pass:", result.passed
    )