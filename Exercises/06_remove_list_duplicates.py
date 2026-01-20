numbers = [5, 6, 2, 7, 6, 5, 3, 1, 2]
unique_numbers = set(numbers)
# print(unique_numbers)

unique_numbers_count = dict()
for number in numbers:
    if unique_numbers_count.get(number) is None:
        unique_numbers_count[number] = 1

print(list(unique_numbers_count.keys()))
