# Iterator object is the behind the scenes mechanism for any loop over container object
# It defines "__next__" method to access the elements in a container object
s = 'abc'
it = iter(s)
print(it)

print(next(it))
print(next(it))
print(next(it))


# print(next(it)) # raises "StopIteration" error

# We can create a custom iterator class implementation by defining "__iter__" method returning an object with a "__next__" method.
# if "__next__" method is defined in the same class then we can return "self" object from the "__iter__" method
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


a = ReverseIterator('spam')
for x in a:
    print(x)
