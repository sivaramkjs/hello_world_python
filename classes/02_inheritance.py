class Vehicle:
    make: str
    model: str
    year: int

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return self.__str__()  # calling derived class method from base class using "self" instance

    def desc(self):
        return f'base -- {self.make} {self.model} {self.year}'


class Car(Vehicle):
    # def __init__(self, make, model, year):
    #     super().__init__(make, model, year)
    #     self.make = make
    #     self.model = model
    #     self.year = year

    def desc(self):
        return Vehicle.__str__(self)  # calling base class method from derived class

    def __str__(self):
        return f'derived -- {self.make} {self.model} {self.year}'


x = Car('BMW', 'iX3', 2026)
print(x.desc())
y = Vehicle('BMW', 'X3', 2025)
print(y.desc())
print(isinstance(x, Vehicle))
print(issubclass(Car, Vehicle))


# Multiple inheritance
class A:
    def who(self): print("A")


class B(A):
    def who(self): print("B"); super().who()  # multiple statements on the same line using ";" semicolon


class C(A):
    def who(self): print("C"); super().who()


# Method Resolution Order (MRO) uses dynamic ordering C3 algorithm and try to create a linear hierarchy by collapsing
# any possible "diamond" problem. This can be combining depth-first, left-right, only-once parent visit strategies
# and satisfying all these constraints
#
#  from diamond:
#     A
#   /  \
#  B    C
#  \   /
#    D
# to linear:
# D->B->C->A
#
# MRO would order as below
# 1. Base class ordering: B->A, C->A
# 2. Derived class ordering: D->B->A, D->C->A.
#    Unique order satisfying these two MROs is D->B->C->A
# 3. In case of not being able to find such MRO will result in an error
class D(B, C):
    pass


# For "class E(C, D)" -  "TypeError: Cannot create a consistent method resolution order (MRO) for bases C, D".
# Below two orders are possible for this
# E->C->A, E->D->B->C->A
# Base class "D" MRO cannot be changed by "E" MRO and "E" must need "C->D" order.
# However, the above MROs doesn't satisfy this constraint for linearization. Hence, it will result in an error
class E(D, C):
    pass


d = D()
d.who()
print(D.__mro__)

e = E()
e.who()
print(E.__mro__)
