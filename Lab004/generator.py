import math

class TrigonomicOperations:
    def __init__(self, initial):
        self.x = initial
        self.i = 0
        self._valid_parameters()

    def _valid_parameters(self):
        if self.x >= 1:
            raise ValueError("x0 >= 1 !")

    def next(self):
        self.x = (1 / math.pi) * math.acos(math.cos((self.i + 100) * self.x))
        self.i = self.i + 1
        return self.x

class Generator:
    def __init__(self, oper):
        self.oper = oper

    def generate(self, n):
        if n <= 0:
            raise ValueError("Size must be greater zero")

        values = []
        for _ in range(n):
            values.append(self.oper.next())
        return values

if __name__ == "__main__":
    oper = TrigonomicOperations(0.1)
    generator = Generator(oper)
    print(generator.generate(5))