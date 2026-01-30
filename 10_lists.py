# List/Tuple is a sequence with defined order of elements and index-based access

names = ["John", "Bob", "Sivaram", "Sravani"]
names[0] = "Jon"
print(names[0])
print(names[-1])
print(names[1:])
print(names[:2])
print(names[-2:])
print(names[:-2])
print(names[0:4:2])
print(names[:])

# Methods
numbers = [5, 2, 3, 6, 3]
numbers2 = numbers.copy()

numbers.insert(2, 10)
numbers.append(14)
numbers.remove(3)
# numbers.reverse()
numbers.pop(1)
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
