# CSE307: Assignment 2

## Part 1: Timing the First Group of Functions

- a.) Average execution time for func_a: 2.7e-07 seconds
- b.) Average execution time for func_b: 5.65e-07 seconds
- c.) Average execution time for func_c: 5.18e-07 seconds
- d.) Average execution time for func_d: 1.28e-06 seconds
- e.) Average execution time for func_e: 1.96e-06 seconds
- f.) Average execution time for func_f: 2.05e-06 seconds
- g.) Average execution time for func_g: 6.19e-06 seconds
- h.) Average execution time for func_h: 6.03e-06 seconds
- i.) Average execution time for func_i: 6.37e-07 seconds

## Part 2: Timing Difference Between Numpy and Native List Building

- a.) Numpy function func_2a_numpy is 0.0013 seconds faster.
- b.) List function func_2b_list is 0.0001 seconds faster.
- c.) Numpy function func_2c_numpy is 9.7e-05 seconds faster.
- d.) Numpy function func_2d_numpy is 0.00022 seconds faster.

## Part 3: What is the Difference Between `range` and `arange`?

Range is a built in python function which returns a range object.
Arange is a numpy function which returns a numpy array.
Unlike range, arange can generate more than just integer values,
by passing a datatype though the dtype parameter.

## Part 4: What is the Difference Between `arange` and `linspace`?

Linspace is similar to arange with one subtle difference.
When using linspace, you specify the number of elements/samples,
and when using arange you specify the size of the steps.
