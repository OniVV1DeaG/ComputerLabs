from Lab003.classes.Extremum import Max
from Lab003.classes.Extremum import Min
from Lab003.classes.Extremum import Derative

class Bisaction:
    _iterations = 0

    @property
    def get_iterations(self):
        return self._iterations

    def _increase_iteration(self):
        self._iterations += 1


    def find_extremum(self, fn, interval, eps = 1e-7):
        a = interval.get_start
        b = interval.get_end
        x = (a + b) / 2

        if Derative(fn, a)() > 0 and Derative(fn, b)() > 0:
            print("No extremum!")
            return

        while abs(Derative(fn, x)()) > eps:
            self._increase_iteration()
            if Derative(fn, x)() < 0:
                a = x
            else:
                b = x
            print(x)
            x = (a + b) / 2

        if Derative(fn, x + eps, False)() > 0:
            print(Min(x, fn(x)))
        else:
            print(Max(x, fn(x)))