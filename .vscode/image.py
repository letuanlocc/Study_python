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
        chaos = int(seq[idx] * 1e6) #Fixed-Point Scaling
        image = int(LL_vec[idx] * 1e6)
        mixed = chaos ^ image ^ (idx * 31) #Entropy Mixing + Position-based perturbation
        for k in range(5):
            bits.append((mixed >> k) & 1)
    bits = np.array(bits, dtype=np.int8)
    return bits
LL_vec = LL_form()
def generate_10_streams(LL_vec):
    streams = []
    x0_values = np.random.uniform(0.001, 0.999, 10)
    for x0 in x0_values:
        bits = generate_bits(LL_vec, x0)
        if len(bits) < 10:
            print("Warning: stream quá ngắn")
        streams.append(bits)
        with open("bits.txt", "w") as f:
            for stream in streams:
                bit_string = ''.join(map(str, stream))
                f.write(bit_string + "\n")
        print("Đã ghi 10 chuỗi bit vào file bits.txt")
    return streams, x0_values
generate_10_streams(LL_vec)