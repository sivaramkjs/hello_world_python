for number in range(1, 10, 2):
    print("Attempt", number, (number) * ".")


# for..else
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
# executes only when the accompanying loop doesn't terminate early with break
# statement
else:
    print("Attempt failed")


# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


# Iterables
print(type(5))
print(type(range(5)))

# Iterable
for x in range(5):
    print(x)

for a in "Python":
    print(a)

# List
for z in [1, 2, 3]:
    print(z)
