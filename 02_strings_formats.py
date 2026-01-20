import math

s = "Hello {0}! How are you?"

print(s.format("Sivaram"))

s1 = "Hello {0:10}! How are you?"  # formatted value with minimum number of characters wide
print(s1.format("Sivaram"))  # string values are left-aligned by default (with added spaces at the ending)
print(s1.format(123))  # integer values are right-aligned by default (with added spaces at the beginning)
# Override spaces alignment
s2 = "Hello {0:>10}! How are you?"  # right
print(s2.format("Sivaram"))
print(s2.format(123))
s3 = "Hello {0:<10}! How are you?"  # left
print(s3.format("Sivaram"))
print(s3.format(123))
s4 = "Hello {0:^10}! How are you?"  # center
print(s4.format("Sivaram"))
print(s4.format(123))

# "=" specifier used to expand an expression to the text of the expression, an equal sign, then the representation of
# the evaluated expression
count = 10
area_name = "USA"
print(f"{area_name=}, {count=}")

# formatted strings
name = "Sivaram"
print(f'Hello {name:10}! How are you?')

# decimal point format specifier
print(f"pi: {math.pi:.4f}")
