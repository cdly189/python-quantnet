"""
A function that returns the Fibonacci sequence as a list
"""


def fibonacci_loop(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        a = 1
        b = 1
        for i in range(n - 1):
            a, b = b, a + b
        return a


# using recursion
def rec_fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        return rec_fib(n - 1) + rec_fib(n - 2)


nth_term = 8


def main():
    # test iterative
    print('Using iterative')
    for x in range(nth_term):
        print(fibonacci_loop(x))

    # test recursion
    print('Using recursion')
    if nth_term < 0:
        print("Please enter a positive integer")
    for x in range(nth_term):
        print(rec_fib(x))


if __name__ == '__main__':
    main()