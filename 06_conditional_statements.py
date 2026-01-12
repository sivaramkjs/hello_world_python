temperature = 15

if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


# Ternary Operator
age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

message = "Eligible" if age >= 18 else "Not eligible"

print(message)


# Logical operators
# and, or, not

high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
