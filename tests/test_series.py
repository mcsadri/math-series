# series tests

from series.series import fibonacci
from series.series import lucas
from series.series import sum_series

#################################################
# test cases for fibonacci sequence numbers
#################################################
def test_fibonacci_exists():
    assert fibonacci

def test_fibonacci_n_equals_seven():
    fib_actual = fibonacci(7)
    fib_expected = 13
    assert fib_actual == fib_expected

def test_fibonacci_n_equals_fourteen():
    fib_actual = fibonacci(14)
    fib_expected = 377
    assert fib_actual == fib_expected

def test_fibonacci_n_equals_negative():
    fib_actual = fibonacci(-3)
    fib_expected = "please enter an integer >= 0"
    assert fib_actual == fib_expected

def test_fibonacci_n_equals_non_int_number():
    fib_actual = fibonacci(3.14)
    fib_expected = "please enter an integer >= 0"
    assert fib_actual == fib_expected

def test_fibonacci_n_equals_string():
    fib_actual = fibonacci("doodah")
    fib_expected = "please enter an integer >= 0"
    assert fib_actual == fib_expected

#################################################
# test cases for Lucas sequence numbers
#################################################
def test_lucas_exists():
    assert lucas

def test_lucas_n_equals_seven():
    luc_actual = lucas(7)
    luc_expected = 29
    assert luc_actual == luc_expected

def test_lucas_n_equals_37():
    luc_actual = lucas(37)
    luc_expected = 54018521
    assert luc_actual == luc_expected

def test_lucas_n_equals_negative():
    luc_actual = lucas(-1)
    luc_expected = "please enter an integer >= 0"
    assert luc_actual == luc_expected

def test_lucas_n_equals_non_int_number():
    luc_actual = lucas(1.41421356237)
    luc_expected = "please enter an integer >= 0"
    assert luc_actual == luc_expected

def test_lucas_n_equals_string():
    luc_actual = lucas("doodah")
    luc_expected = "please enter an integer >= 0"
    assert luc_actual == luc_expected


#################################################
# test cases for Lucas sequence numbers
#################################################
def test_sum_series_exists():
    assert sum_series