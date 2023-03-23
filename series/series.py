# find the nth term of the Fibonacci sequence iteratively, uses optional params for non-Fibonacci series
def fibonacci(n, x = 0, y = 1):
    """
    :param n: required, function calculates this nth position of numerical series
    :param x: optional; 1st number of series to calculate; defaults to 0 for Fibonacci
    :param y: optional, 2nd number of series to calculate; defaults to 1 for Fibonacci
    :return: nth term of Fibonacci sequence
    """
    if isinstance(n, int) and isinstance(x, int) and isinstance(y, int) and n >= 0:
        fib_list = [x, y]
        i = 0
        while i < (n - 1):
            fib_list.append(fib_list[i] + fib_list[i + 1])
            i += 1
        return fib_list[n]
    else:
        return "please enter an integer >= 0"

# find the nth term of the Lucas sequence recursively
# recursive solution assisted by ChatGPT
def lucas(n):
    """
    :param n:
    :return: nth number of Lucas sequence
    """
    if not isinstance(n, int) or n < 0:
        return "please enter an integer >= 0"
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

# find the nth term of a user specified series with 1 required and 2 optional parameters
def sum_series(n, x = 0, y = 1):
    """
    :param n: required, function calculates this nth position of numerical series
    :param x: optional; 1st number of series to calculate; defaults to 0 for Fibonacci
    :param y: optional, 2nd number of series to calculate; defaults to 1 for Fibonacci
    :return: nth term of calculated series
    """
    return fibonacci(n, x, y)
