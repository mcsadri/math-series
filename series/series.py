#def main():
#    fibonacci(7)

# find the nth term of the Fibonacci sequence iteratively
def fibonacci(n):
    """
    :param n:
    :return: nth term of Fibonacci sequence
    """
    if isinstance(n, int) and n >= 0:
        fib_list = [0, 1]
        i = 0
        while i < (n - 1):
            fib_list.append(fib_list[i] + fib_list[i + 1])
            i += 1
        #print(fib_list[n])
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
def sum_series():
    pass

#main()