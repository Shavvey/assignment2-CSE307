import timeit as t

# example to show how the timeit function works
def example_func():
    return [list(range(i, i + 3)) for i in [10, 20, 30]]


def time(function_name: str, number_itrs: int | None = None) -> float:
    if number_itrs != None:
        return t.timeit(setup=f"from __main__ import {function_name}")
    else:
        return t.timeit(setup=f"from __main__ import {function_name}")


def main():
    print(time(example_func.__name__, 10000))


if __name__ == "__main__":
    main()
