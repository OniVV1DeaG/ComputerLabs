import math

from Lab003.classes.Extremum import Max
from Lab003.classes.Extremum import Min
from Lab003.classes.Extremum import Derative


class NewTone:
    _iterations = 0

    @property
    def get_iterations(self):
        return self._iterations

    def _increase_iteration(self):
        self._iterations += 1


    def find_extremum(self, fn, interval, min, derat, eps = 1e-7):
        a = interval.get_start
        b = interval.get_end
        x = a

        if Derative(fn, a)() > 0 and Derative(fn, b)() > 0:
            print("No extremum!")
            return

        while abs(Derative(fn, x)()) > eps:
            self._increase_iteration()
            x = x - (Derative(fn, x)()/Derative(derat, x)())
            print(x)

        if Derative(fn, x + eps, False)() > 0:
            print(Min(x, fn(x)))
        else:
            print(Max(x, fn(x)))





