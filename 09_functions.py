def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard")


# Two lines breaks recommended
greet("Sivaram", "Koduri")
greet("John", "Smith")


def get_greeting(name):
    return f"Hello {name}"


message = get_greeting("Sivaram")


# Keyword/Named arguments
def increment(number, by):
    return number + by


print(increment(2, by=1))  # <--


# Default arguments
def decrement(number, by=1):
    return number - by


print(decrement(2))


# *args (packing unbounded list of arguments)
def multiply(*numbers):
    product = 1
    for number in numbers:
        product *= number

    return product


print(multiply(2, 3, 4, 5))
print(multiply(*[2, 3, 4, 5]))


# packing multiple keyword arguments
def add_kw(**kwargs):
    final_sum = 0
    for v in kwargs.values():
        final_sum += v

    return final_sum


print(add_kw(**{'a': 2, 'b': 4}))  # unpacking dictionary into keyword arguments
print(add_kw(a=5, b=6))  # multiple keyword arguments


# Unpacking list into positional arguments
def add(a, b):
    return a + b


nums = [1, 2]
print(add(*nums))


# Unpacking dict into keyword arguments
def add1(a, b):
    return a + b


nums1 = {"a": 1, "b": 2}
print(add1(**nums1))


# Lambda functions
def divide(a, b):
    return lambda: a / b


func = divide(3, 2)
print(func())
