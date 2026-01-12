# >, >=, <, <=, ==, !=

print(10 == "10")
print(10 != "10")

print("bag" > "apple")  # Alphabetical/ASCII codes

print("bag" == "BAG")

print(f"ASCII - b: {ord("b")}, B: {ord("B")}")

# Chaining comparison operators
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")
