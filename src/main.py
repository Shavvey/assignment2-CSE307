import timeit as t
import numpy as np
from time import sleep


# example to show how the timeit function works
def example_func():
    return [list(range(i, i + 3)) for i in [10, 20, 30]]


# NOTE: args is a variatic array of the arguments we need to pass to the function
def time(function_name: str, *args, number_itrs: int | None = None) -> float:
    args = "".join([str(arg) + ", " for arg in args]).strip(", ")
    print(args)
    if number_itrs != None:
        return t.timeit(
            f"{function_name}({args})",
            setup=f"from __main__ import {function_name}",
            number=number_itrs,
        )
    else:
        return t.timeit(
            f"{function_name}({args})", setup=f"from __main__ import {function_name}"
        )


def func_a():
    return np.array([1, 2, 3, 4, 5])


def func_b(n: int):
    return np.array(list(range(0, n + 1)))


def func_c(n: int):
    return np.array(list(range(0, 3 * (n + 1), 3)))


def main():
    number_itrs = 10_000
    exec_time = time(func_b.__name__, 10, number_itrs=number_itrs) / number_itrs
    print(f"Average Execution Time: {exec_time:.3} seconds")


if __name__ == "__main__":
    main()
