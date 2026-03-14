import cv2
import pywt
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare


class ImageProcessor:
    def __init__(self, path):
        self.path = path
        self.image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if self.image is None:
            raise ValueError("Không đọc được ảnh")
    def get_LL_vector(self):
        img = np.float32(self.image)
        LL, _ = pywt.dwt2(img, 'haar')
        LL_norm = (LL - LL.min()) / (LL.max() - LL.min())
        print("Kích thước LL:", LL.shape)
        return LL_norm.flatten()
    def total_positions(self):
        h, w = self.image.shape
        return h * w
class ChaoticGenerator:
    def __init__(self, r=3.99, x0=0.318):
        self.r = r
        self.x = x0
    def logistic_map(self, N):
        seq = np.zeros(N)
        for _ in range(1000):
            self.x = self.r * self.x * (1 - self.x)
        for i in range(N):
            self.x = self.r * self.x * (1 - self.x)
            seq[i] = self.x
        return seq
    def generate_bits(self, LL_vec):
        seq = self.logistic_map(len(LL_vec))
        bits = []
        for i in range(len(seq) - 1):
            f1 = seq[i] - LL_vec[i]
            f2 = seq[i + 1] - LL_vec[i + 1]
            if f1 * f2 < 0:
                chaos = int(seq[i] * 1e6)
                image = int(LL_vec[i] * 1e6)
                mixed = chaos ^ image ^ (i * 31)
                for k in range(5):
                    bits.append((mixed >> k) & 1)
        return bits
class PositionGenerator:
    def bits_to_integers(self, bits, chunk_size=32):
        usable_len = len(bits) // chunk_size * chunk_size
        bits = bits[:usable_len]
        numbers = []
        for i in range(0, usable_len, chunk_size):
            val = 0
            for j in range(chunk_size):
                val = (val << 1) | bits[i + j]
            numbers.append(val)
        return np.array(numbers, dtype=np.uint32)
    def generate_positions(self, numbers32, total_positions, payload_size=None):
        limit = (2**32 // total_positions) * total_positions
        positions = []
        valid_numbers = []
        for x in numbers32:
            if x < limit:
                positions.append(x % total_positions)
                valid_numbers.append(x)
        positions = np.array(positions)
        valid_numbers = np.array(valid_numbers)
        positions, unique_idx = np.unique(positions, return_index=True)
        valid_numbers = valid_numbers[unique_idx]
        order = np.argsort(valid_numbers)
        positions = positions[order]
        if payload_size is not None:
            positions = positions[:payload_size]
        return positions.astype(np.uint32)
class StatisticalTester:
    def uniform_test(self, data):
        plt.figure(figsize=(8,4))
        plt.hist(data, bins=50, edgecolor='black')
        plt.title("Histogram of Embedding Positions")
        plt.show()
        counts, _ = np.histogram(data, bins=50)
        chi, p = chisquare(counts)
        print("Chi-square:", chi)
        print("p-value:", p)
        if p > 0.05:
            print("→ PASS uniform distribution")
        else:
            print("→ FAIL uniform distribution")
    def serial_correlation_test(self, data):
        corr = np.corrcoef(data[:-1], data[1:])[0,1]
        print("\nSerial correlation:", corr)
        if abs(corr) < 0.05:
            print("→ Independence rất tốt")
        elif abs(corr) < 0.1:
            print("→ Independence chấp nhận được")
        else:
            print("→ Có dấu hiệu phụ thuộc")
        plt.figure(figsize=(5,5))
        plt.scatter(data[:-1], data[1:], s=1)
        plt.title("Serial Scatter Plot")
        plt.xlabel("x(i)")
        plt.ylabel("x(i+1)")
        plt.show()
    def gap_test(self, data):
        print("\n===== GAP TEST =====")
        low = np.min(data)
        high = np.max(data)
        region_start = low + (high-low)*0.3
        region_end = low + (high-low)*0.6
        gaps = []
        gap = 0
        for x in data:

            if region_start <= x <= region_end:
                gaps.append(gap)
                gap = 0
            else:
                gap += 1
        if len(gaps) == 0:
            print("Không đủ dữ liệu gap test")
            return
        plt.figure(figsize=(8,4))
        plt.hist(gaps, bins=30, edgecolor='black')
        plt.title("Gap Distribution")
        plt.show()
        print("Mean gap:", np.mean(gaps))
        print("Std gap:", np.std(gaps))
        print("→ Nếu histogram giảm dần dạng geometric là tốt")
# ===== MAIN PIPELINE =====
image = ImageProcessor("example2.png")
LL_vec = image.get_LL_vector()
chaos = ChaoticGenerator()
bits = chaos.generate_bits(LL_vec)
posGen = PositionGenerator()
numbers = posGen.bits_to_integers(bits)
positions = posGen.generate_positions(
    numbers,
    image.total_positions(),
    payload_size=5000
)
print("Embedding positions:", positions[:20])
print("Total usable:", len(positions))
with open("positions.txt", "w") as f:
    for p in positions:
        f.write(str(p) + "\n")
tester = StatisticalTester()    
tester.uniform_test(positions)
tester.serial_correlation_test(positions)
tester.gap_test(positions)