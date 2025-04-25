import numpy as np

class GeoGenerator:
    def generate(self,p, size):
        if size <= 0:
            raise ValueError("size >= 0!")

        return np.random.geometric(p, size)

if __name__ == "__main__":
    gg = GeoGenerator()
    print(gg.generate(2, 20))