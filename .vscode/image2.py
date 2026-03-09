import cv2
import pywt
import numpy as np
from nistrng import SP800_22R1A_BATTERY, check_eligibility_all_battery, run_all_battery
def LL_form(path="example2.png"):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Không đọc được ảnh")
    image = np.float32(image)
    LL, (LH, HL, HH) = pywt.dwt2(image, 'haar')
    print("Kích thước LL:", LL.shape)
    LL_norm = (LL - LL.min()) / (LL.max() - LL.min())
    return LL_norm.flatten()
def logistic_map(N):
    r = 3.99
    x = 0.318
    seq = np.zeros(N)
    for _ in range(1000):
        x = r * x * (1 - x)
    for i in range(N):
        x = r * x * (1 - x)
        seq[i] = x

    return seq
def generate_bits(LL_vec):
    seq = logistic_map(len(LL_vec))
    intersections = []
    for i in range(len(seq) - 1):
        f1 = seq[i] - LL_vec[i]
        f2 = seq[i+1] - LL_vec[i+1]
        if f1 * f2 < 0:
            intersections.append(i)
    bits = []
    numbers = []
    chunk_size = 20
    for idx in intersections:
        chaos = int(seq[idx] * 1e6)
        image = int(LL_vec[idx] * 1e6)
        mixed = chaos ^ image ^ (idx * 31)
        for k in range(5):
            bits.append((mixed >> k) & 1)
        # bit_len = (mixed % 18) + 3 #mixed chia dư cho n thì luôn bé hơn n -> +3 để trong khoảng 3 ->20
        # mask = (1 << bit_len) - 1 # các bit cuối thay đổi nhiều hơn entropy cao hơn
        # rand_val = mixed & mask
        # rand_val = rand_val % 1000000 + 1 # đảm bảo kết quả luôn < 1000000 
        # bits.append(rand_val)
    for i in range(0, len(bits), chunk_size):
        val = 0

        for j in range(chunk_size):
            if i + j < len(bits):
                val = (val << 1) | bits[i+j]

        val = val % 10000 + 1   # đảm bảo 1 → 9999
        numbers.append(val)
    # bits = np.array(bits, dtype=np.int8)
    # bit_string = ''.join(map(str, bits))
    # with open("bits.txt", "w") as f:
    #     f.write(bit_string)
    #     print("Đã ghi chuỗi bit vào file bits.txt")
    return numbers
# ===== MAIN =====
LL_vec = LL_form()
bits = generate_bits(LL_vec)
print("Số bit:", len(bits))
print(bits)
# print("\n===== NIST TEST =====")
# eligible_tests = check_eligibility_all_battery(bits, SP800_22R1A_BATTERY)
# results = run_all_battery(bits, eligible_tests)
# for result, elapsed in results:
#     print(result.name, "score:", result.score, "pass:", result.passed)