import math

from Lab003.classes.Extremum import IntervalSearch
from Lab003.classes.Function import Function
from Lab003.classes.NewTone import NewTone
from Lab003.classes.Extremum import Interval
from Lab003.classes.Bisaction import Bisaction
from Lab003.classes.Graphic import Graphic

if __name__ == "__main__":
    #fn = Function(lambda x: math.e ** (-x) * math.asin(math.e ** x))
    fn = Function(lambda x: x ** 2 + 3*x + 2)
    interval = Interval(-6, 6)
    find_int = IntervalSearch(fn, 1, interval)
    print(find_int.find_extremum_intervals())
    graphic = Graphic(fn, interval, 1)
    graphic.create()

    epsilons = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10, 1e-11, 1e-12, 1e-13, 1e-14, 1e-15]

    nt = NewTone()
    bs = Bisaction()
    for epsilon in epsilons:
        try:
            nt.find_extremum(fn, interval, True, lambda x: 2*x + 3)
            print(f"Iteration of NewTone: {nt.get_iterations}")
        except Exception as e:
            pass

        try:
            bs.find_extremum(fn, interval, True)
            print(f"Iteration of Bisaction: {bs.get_iterations}")
        except Exception as e:
            print("yes")
            pass