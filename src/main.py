import timeit as t
import numpy as np


# example to show how the timeit function works
def example_func():
    return [list(range(i, i + 3)) for i in [10, 20, 30]]


# NOTE: args is a variatic array of the arguments we need to pass to the function
def time(function_name: str, *args, number_itrs: int | None = None) -> float:
    args = "".join([str(arg) + ", " for arg in args]).strip(", ")
    if number_itrs != None:
        if number_itrs <= 0:
            raise ValueError(
                "[ERROR]: number_itrs must be some positive value larger than zero!"
            )
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
    return np.array(list(range(1, n + 1)))


def func_c(n: int):
    return np.array(list(range(0, 3 * (n + 1), 3)))


def func_d():
    return np.array([[x for x in range(i, i + 4)] for i in range(1, 4)])


def func_e(n: int):
    return np.array([[x for x in range(i, n + i)] for i in range(1, 4)])


def func_f(n: int):
    return np.array(
        [[j for j in range(1 + n * (i - 1), n * i + 1)] for i in range(1, 4)]
    )


def func_g(n: int, m: int):
    return np.array([[j for j in range(1 + i, n + i + 1)] for i in range(0, m)])


def func_h(n: int, m: int):
    return np.array(
        [[j for j in range(1 + n * (i - 1), n * i + 1)] for i in range(1, m + 1)]
    )


def func_i(n: int):
    return np.array([0 for _ in range(0, n)])


def print_funcs():
    print(func_a())
    print()
    print(func_b(10))
    print()
    print(func_c(10))
    print()
    print(func_d())
    print()
    print(func_e(10))
    print()
    print(func_f(10))
    print()
    print(func_g(10, 10))
    print()
    print(func_h(10, 10))
    print()
    print(func_i(10))


def func_timing():
    number_itrs = 1000
    avg_exec_time = time(func_a.__name__, number_itrs=number_itrs) / number_itrs
    print(f"Average execution time for func_a: {avg_exec_time:.3} seconds")
    avg_exec_time = time(func_b.__name__, 10, number_itrs=number_itrs) / number_itrs
    print(f"Average execution time for func_b: {avg_exec_time:.3} seconds")
    avg_exec_time = time(func_c.__name__, 10, number_itrs=number_itrs) / number_itrs
    print(f"Average execution time for func_c: {avg_exec_time:.3} seconds")
    avg_exec_time = time(func_d.__name__, number_itrs=number_itrs) / number_itrs
    print(f"Average execution time for func_d: {avg_exec_time:.3} seconds")
    avg_exec_time = time(func_e.__name__, 10, number_itrs=number_itrs) / number_itrs
    print(f"Average execution time for func_e: {avg_exec_time:.3} seconds")
    avg_exec_time = time(func_f.__name__, 10, number_itrs=number_itrs) / number_itrs
    print(f"Average execution time for func_f: {avg_exec_time:.3} seconds")
    avg_exec_time = time(func_g.__name__, 10, 10, number_itrs=number_itrs) / number_itrs
    print(f"Average execution time for func_g: {avg_exec_time:.3} seconds")
    avg_exec_time = time(func_h.__name__, 10, 10, number_itrs=number_itrs) / number_itrs
    print(f"Average execution time for func_h: {avg_exec_time:.3} seconds")
    avg_exec_time = time(func_i.__name__, 10, number_itrs=number_itrs) / number_itrs
    print(f"Average execution time for func_i: {avg_exec_time:.3} seconds")


def func_2a_numpy(n: int):
    return np.zeros(n)


def func_2a_list(n: int):
    l = [0 for _ in range(n)]
    return np.array(l)


def func_2b_numpy(n: int):
    return np.ones(n)


def func_2b_list(n: int):
    l = [1 for _ in range(n)]
    return np.array(l)


def func_2c_numpy(n: int):
    return np.full(n, fill_value=5)


def func_2c_list(n: int):
    l = [5 for _ in range(n)]
    return np.array(l)


def func_2d_numpy(a: int, n: int, d: int):
    return np.arange(a, a + (n + 1) * d, d)


def func_2d_list(a: int, n: int, d: int):
    l = [a + i * d for i in range(n + 1)]
    return np.array(l)


def print_funcs2():
    print(func_2a_list(10))
    print(func_2a_numpy(10))
    print(func_2b_list(10))
    print(func_2b_numpy(10))
    print(func_2c_list(10))
    print(func_2c_numpy(10))
    print(func_2d_list(10, 3, 4))
    print(func_2d_numpy(10, 3, 4))


def print_time_difference(func_name: str, difference: float):
    if difference > 0:
        print(f"Numpy function {func_name}_numpy is {difference:.2} seconds faster.")
    else:
        print(f"List function {func_name}_list is {-1*difference:.2} seconds faster.")



def func2_timing():
    number_itrs = 1000
    a2_list_time = time(func_2a_list.__name__, 10, number_itrs=number_itrs)
    a2_numpy_time = time(func_2a_numpy.__name__, 10, number_itrs=number_itrs)
    difference = a2_list_time - a2_numpy_time
    # NOTE: dumb strip to get rid of numpy postfix in function
    print_time_difference(func_2a_numpy.__name__.strip("_numpy"), difference)
    b2_list_time = time(func_2b_list.__name__, 10, number_itrs=number_itrs)
    b2_numpy_time = time(func_2b_numpy.__name__, 10, number_itrs=number_itrs)
    difference = b2_list_time - b2_numpy_time
    print_time_difference(func_2b_numpy.__name__.strip("_numpy"), difference)
    c2_list_time = time(func_2c_list.__name__, 10, number_itrs=number_itrs)
    c2_numpy_time = time(func_2c_numpy.__name__, 10, number_itrs=number_itrs)
    difference = c2_list_time - c2_numpy_time
    print_time_difference(func_2c_numpy.__name__.strip("_numpy"), difference)
    d2_list_time = time(func_2d_list.__name__, 10, 3, 4, number_itrs=number_itrs)
    d2_numpy_time = time(func_2d_numpy.__name__, 10, 3, 4, number_itrs=number_itrs)
    difference = d2_list_time - d2_numpy_time
    print_time_difference(func_2d_numpy.__name__.strip("_numpy"), difference)


def main():
    func_timing()
    func2_timing()


if __name__ == "__main__":
    main()
