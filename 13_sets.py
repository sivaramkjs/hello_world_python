a = set()  # unordered collection, contain unique items
a = {1}
a.add(2)
a.add(2)
b = a.union({3, 4})

print(b)
print(5 not in b)
print(4 in b)

print(set('abracadabra'))

# Set Comprehensions
c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)

y = {'abracadabra', 'pqr'}
d = {x[i] for x in y for i in range(3)}
print(d)
