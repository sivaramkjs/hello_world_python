numbers = [5, 2, 5, 2, 2] # Letter F

# for number in numbers:
#     print("x" * number)
for number in numbers:
    shape = ""
    for x in range(number):
        shape += "x"
    print(shape)