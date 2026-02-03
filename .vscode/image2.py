import hashlib
import random
import numpy as np

class IndexGenerator:
    def __init__(self, key: str, max_range: int):
        self.key = key
        self.max_range = max_range

        # key -> seed
        h = hashlib.sha256(key.encode()).hexdigest()
        self.seed = int(h, 16) % (2**31)

    def generate_indices(self, n_indices: int):
        """
        Sinh vị trí giả ngẫu nhiên dựa trên key
        """
        random.seed(self.seed)

        indices = random.sample(
            range(self.max_range),
            n_indices
        )
        return sorted(indices)

    def analyze(self, indices):
        """
        Phân tích phân bố
        """
        gaps = np.diff(indices)

        return {
            "total": len(indices),
            "min_gap": int(np.min(gaps)),
            "max_gap": int(np.max(gaps)),
            "avg_gap": float(np.mean(gaps)),
            "std_gap": float(np.std(gaps)),
            "consecutive": int(np.sum(gaps == 1))
        }


# ================== TEST ==================
if __name__ == "__main__":
    key = "Locbitnot2k6@"
    max_range = 5000
    n_indices = 100

    gen = IndexGenerator(key, max_range)

    indices = gen.generate_indices(n_indices)
    stats = gen.analyze(indices)

    print("KEY:", key)
    print("FIRST 10 INDICES:", indices[:10])
    print("LAST 10 INDICES:", indices[-10:])

    print("\n📊 DISTRIBUTION:")
    for k, v in stats.items():
        print(f"{k:12s}: {v}")