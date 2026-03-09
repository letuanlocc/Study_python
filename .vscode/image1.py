import cv2
import pywt
import numpy as np
def LL_form(path="example2.png"):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Không đọc được ảnh")
    image = np.float32(image)
    LL, (LH, HL, HH) = pywt.dwt2(image, 'haar')
    print("Kích thước LL:", LL.shape)
    LL_norm = (LL - LL.min()) / (LL.max() - LL.min())
    return LL_norm.flatten()
def logistic_map(N, x0):
    r = 3.99
    x = x0
    seq = np.zeros(N)
    for _ in range(1000):
        x = r * x * (1 - x)
    for i in range(N):
        x = r * x * (1 - x)
        seq[i] = x
    return seq
# ===== Generate bits =====
def generate_bits(LL_vec, x0):
    seq = logistic_map(len(LL_vec), x0)
    intersections = []
    for i in range(len(seq) - 1):
        f1 = seq[i] - LL_vec[i]
        f2 = seq[i+1] - LL_vec[i+1]
        if f1 * f2 < 0:
            intersections.append(i)
    bits = []
    for idx in intersections:
        chaos = int(seq[idx] * 1e6)
        image = int(LL_vec[idx] * 1e6)
        mixed = chaos ^ image ^ (idx * 31)
        for k in range(5):
            bits.append((mixed >> k) & 1)
    bits = np.array(bits, dtype=np.int8)
    return bits
# ===== Generate many bitstreams =====
def generate_streams(LL_vec, num_streams=100, target_bits=1000000):
    streams = []
    with open("nist_streams.txt", "w") as f:
        for i in range(num_streams):
            print("\nGenerating stream", i+1)
            bits = []
            while len(bits) < target_bits:
                x0 = np.random.uniform(0.2, 0.8)
                new_bits = generate_bits(LL_vec, x0)
                bits.extend(new_bits)
            bits = bits[:target_bits]
            bits = np.array(bits, dtype=np.int64)
            streams.append(bits)
            bit_string = ''.join(map(str, bits))
            f.write(bit_string + "\n")
            print("Stream", i+1, "bits:", len(bits))
    print("\nSaved file: nist_streams.txt")
    return streams
# ===== MAIN =====
LL_vec = LL_form()
streams = generate_streams(LL_vec, num_streams=10, target_bits=1000000)
print("\nQuick test first stream")