# Set/Dictionary is a collection without any order of elements and no index-based access

a = set()  # unordered collection, contain unique items
a = {1}
a.add(2)
a.add(2)
a.remove(2)  # KeyError if not present
a.discard(3)  # Safe remove without error if not present
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
