a = {}
a = {"x": 1, "y": 2}
print(a)

a["y"] = 4
a["z"] = 3
print(a)

del a["y"]
print(a)

# print(a["y"])  # KeyError
print(a.get("y"))  # Returns None
print(a.get("y", 0))  # Returns default value

print(list(a))
print(sorted(a, reverse=True))
print("y" in a)

b = dict([('a', 1), ('b', 2)])
print(b)

# keyword arguments
c = dict(a=1, b=2)
print(c)

# Dict Comprehension
d = {x: x ** 2 for x in (2, 3, 4)}
print(d)

# Looping
# key and value at the same time
for k, v in d.items():
    print(f'{k}:{v}', end=', ')
