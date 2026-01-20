numbers = [12, 5, 18, 1, 3]
current_max = numbers[0]

for number in numbers:
    current_max = number if(number > current_max) else current_max
print(current_max)
