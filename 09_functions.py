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


# *args (unbounded list of arguments)
def multiply(*numbers):
    product = 1
    for number in numbers:
        product *= number

    return product


print(multiply(2, 3, 4, 5))


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
