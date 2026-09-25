# List/Tuple is a sequence with defined order of elements and index-based access

names = ["John", "Bob", "Sivaram", "Sravani"]
names[0] = "Jon"
print(f'{names[0]=}')
print(f'{names[-1]=}')
print(f'{names[1:]=}')  # Slicing
print(f'{names[:2]=}')
print(f'{names[-2:]=}')  # becomes names[len(names) - 2:]
print(f'{names[::-1]=}')  # reverse
print(f'{names[:-2]=}')  # becomes names[:len(names) - 2]
print(f'{names[0:4:2]=}')
print(f'{names[:]=}')

# Methods
numbers = [5, 2, 3, 6, 3]
numbers2 = numbers.copy()

numbers.insert(2, 10)
numbers.append(14)  # single item
numbers.extend([6, 7, 8])  # multiple items
numbers.remove(3)
# numbers.reverse()
print(numbers.pop(1))
print(numbers)
print(numbers.index(3))
print(50 in numbers)
print(numbers.count(3))
numbers.sort(reverse=True)
print(numbers)
print(numbers2)

# Looping
# index and value at the same time
for index, num in enumerate(numbers):
    print(f'[{index}]: {num}')

# List Comprehensions (listcomp)
print([x ** 2 for x in range(1, 10, 2)])

a = [[1, 2, 3], [4, 5, 6]]
print([num for element in a for num in element])

# Nested listcomps
print([[row[i] for row in a] for i in range(3)])

# The below code causes infinite recursion due to circular referencing
# i.e., a = [a] -> a[0] = a -> a[0][0] = a and so on.
# Python represents this using "[...]" notation instead of RecursionError
a = []
a.append(a)
print(a)  # [[...]]

a = [[]] * 3  # same object reference for all inner lists
a[0].append(1)
print(a)

a = [[] for _ in range(3)]
a[0].append(1)
print(a)

a = [0] * 3
print(a)

print(1 | 2 | 2)
print(2 & 2)
print(1 ^ 2 ^ 2)
