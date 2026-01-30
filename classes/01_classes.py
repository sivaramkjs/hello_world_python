def func1(self):
    return "func1"


class MyClass:
    """A class will have attributes, which are defined inside this class definition(namespace).
    There are two kinds of "instance" attributes (bound to a class instance):
    1. Data attributes/Instance variables (E.g., "i")
    2. Methods (E.g., "func()")
    """

    # Class variable shared by all instances of the class. This can be overridden by a specific instance variable if
    # re-assigned
    i = 0

    f = func1  # function definition need not be present in the class. However, this is not recommended to avoid confusion

    # Private instance variables
    # Python "Name Mangling" will rename this to "_MyClass__Spam" to avoid name clashes with any subclass private variables
    __spam = 'I\'m a private instance variable'

    # readonly Property without below setter
    @property
    def full_name(self):
        return self._full_name

    # setter for the above property
    @full_name.setter
    def full_name(self, val):
        self._full_name = val

    def __init__(self, first_name, last_name):
        # Instance variables unique to each instance of the class
        self._full_name = f'{first_name} {last_name}'  # private backing field by convention ('_')
        self.first_name = first_name
        self.last_name = last_name

    def func(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def external_func(self):
        return self.f(self)


a = MyClass("Sivaram", "K")
# Instance/Data attributes (variables) can be assigned dynamically without declaring them in the class definition.
# However, they will be available only in this instance
a.age = 12
# b = MyClass("S", "K")
# print(b.age) # Attribute error since "age" will not be present in the "b" instance

# This is called a "method" attribute bound to the instance "a" but the actual "MyClass.func" is called a "function
# object" since it's not bound to any instance.
# In simple terms, function bound to a class instance is called a "method" and a plain function definition inside class is called a "function"
a.func()  # Equivalent to MyClass.func(a)
MyClass.func(a)

print(a.func.__self__, a.func.__func__)  # Method object attributes

print(a.__class__, type(a))

print(a.i, a.__doc__)
a.i = 123
print(a.i)

print(a.full_name)
a.full_name = 'SR'  # Result in "no setter" error without accompanying setter
print(a.full_name)

print(a._MyClass__spam)
# print(a.__spam) # Can't be accessed due to name mangling
