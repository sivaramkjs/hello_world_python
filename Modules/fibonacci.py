import sys


def fib_nums_up_to(n):  # Fibonacci numbers up to "n"
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


def n_fib_nums(n):  # First "n" Fibonacci numbers
    a, b = 0, 1
    i = 0
    while i < n:
        print(a, end=' ')
        a, b = b, a + b
        i += 1


if __name__ == "__main__":
    fib_nums_up_to(int(sys.argv[1]))
