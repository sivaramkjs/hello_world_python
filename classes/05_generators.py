# Generators can also be used to create an iterator implementation.
# However, with generators, "__iter__" and "__next__" methods are automatically generated and
# method snapshot state is saved automatically between iterations without the need for any local instance variables.
# Additionally, "StopIteration" is raised automatically when they terminate.
# In short, generator is a concise way to create an iterator
import random


def reverse(s):
    for index in range(len(s) - 1, -1, -1):
        yield s[index]  # generator


for a in reverse('spam'):
    print(a)


def split_chunk(data, chunk_size=10):
    while len(data) >= chunk_size:
        yield data[:chunk_size]
        data = data[chunk_size:] if len(data) >= chunk_size else data
    else:
        yield data


d = [random.randrange(1, 20, 2) for _ in range(31)]
print(d)
for chunk in split_chunk(d):
    print(chunk)

# Generator expressions
# More compact way to create simple generator functions
# The syntax is similar to listcomp but using '()' instead of '[]' in listcomp
#
# Difference between a listcomp and generator expression: generator expression will not create an entire list in
# memory. Instead, it yields one element at a time to the iterator. Hence, more memory-friendly

gen = (i * i for i in range(10))
print(gen)  # generator expression describing the sequence to generate
print(sum(gen))
# We can also use generator expression directly in place of the function argument without explicit outer parenthesis.
# Python automatically recognizes the argument as generator for any function call with syntax "func(expr for item in iterable)"
print(sum(i * i for i in range(10)))

x = 'spam'
rev = (x[i] for i in range(len(x) - 1, -1, -1))
print(list(rev))
