import fibonacci

print(fibonacci.fib_nums_up_to(10))
print(fibonacci.n_fib_nums(10))

# import variation 1
from fibonacci import *

print(fib_nums_up_to(10))
print(n_fib_nums(10))

# import variation 2
from fibonacci import fib_nums_up_to, n_fib_nums

print(fib_nums_up_to(10))
print(n_fib_nums(10))

# import variation 3
import fibonacci as fib

print(fib.fib_nums_up_to(10))
print(fib.n_fib_nums(10))

# import variation 4
from fibonacci import fib_nums_up_to as fib1, n_fib_nums as fib2

print(fib1(10))
print(fib2(10))
