# type conversion
# int(x)
# float(x)
# bool(x)
# str(x)

x = input("x: ")  # returns string
# print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")

# bool(x)
# Falsy values
# ""
# 0
# None
print(bool(""))
print(bool("False"))  # Non-empty string -> Truthy value
