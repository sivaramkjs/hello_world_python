a = ()  # empty tuple
b = "hello",  # single item tuple defined with a trailing comma

c = (1, 1.5, "Hi")  # heterogeneous sequence of items unlike homogeneous sequence as list

print(c[:2])

# packing
d = 1, 1.5, "hi"
print(d)

# unpacking
e, f, g = d
print(e, f, g)

# Looping
numbers = [5, 2, 3, 6, 3]
numbers2 = numbers.copy()
numbers.sort()

# Iterating multiple sequences at the same time
# "zip()" returns a tuple containing an item at the same index from each sequence in an iteration
for num1, num2 in zip(numbers, numbers2):
    print(f'num1: {num1}, num2: {num2}', end=', ')
