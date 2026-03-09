import cv2
import pywt
import numpy as np
from nistrng import SP800_22R1A_BATTERY, check_eligibility_all_battery, run_all_battery


# ===== Extract LL feature =====
def LL_form(path="example2.png"):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise ValueError("Không đọc được ảnh")

    image = np.float32(image)

    LL, (LH, HL, HH) = pywt.dwt2(image, 'haar')

    print("Kích thước LL:", LL.shape)

    LL_norm = (LL - LL.min()) / (LL.max() - LL.min())

    return LL_norm.flatten()


# ===== Logistic map =====
def logistic_map(N):
    r = 3.99
    x = 0.441
    seq = np.zeros(N)
    for i in range(N):
        x = r * x * (1 - x)
        seq[i] = x

    return seq


# ===== Generate bits =====
def generate_bits(LL_vec):

    seq = logistic_map(len(LL_vec))

    # threshold = 0.1
    intersections = []

    # for i in range(len(seq)):
    #     if abs(seq[i] - LL_vec[i]) < threshold:
    #         intersections.append((i, seq[i]))
    for i in range(len(seq)-1):
        f1 = seq[i] - LL_vec[i]
        f2 = seq[i+1] - LL_vec[i+1]
        if f1 * f2 < 0:
            intersections.append((i,seq[i]))
    bits = []

    for idx, value in intersections:
        chaos = int(seq[idx] * 1e6)
        image = int(LL_vec[idx] * 1e6)
        mixed = chaos ^ image  ^ (idx * 31)
        # bits.append((mixed >> 8) & 1)
        for k in range(5):
            bits.append((mixed >> k) & 1)   
    bits = np.array(bits, dtype=np.int8)
    bits = bits.astype(np.int64)
    bit_string = ''.join(map(str, bits))
    with open("bits.txt", "w") as f:
        f.write(bit_string)
        print("Đã ghi chuỗi bit vào file bits.txt")
    return bits
# ===== MAIN =====
LL_vec = LL_form()
bits = generate_bits(LL_vec)

print("Số bit:", len(bits))

print("\n===== NIST TEST =====")

eligible_tests = check_eligibility_all_battery(bits, SP800_22R1A_BATTERY)

results = run_all_battery(bits, eligible_tests)
for result, elapsed in results:
    print(result.name, "score:", result.score, "pass:", result.passed)