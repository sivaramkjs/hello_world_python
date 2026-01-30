from dataclasses import dataclass


# "dataclass" provides a syntactic sugar to create a class by auto-generating
# some boilerplate code like "__init__", "__eq__" methods.
# While it's same as class, it's useful for Data Transfer Object (DTO) types
@dataclass  # This is called a "decorator"
class Employee:
    id: int
    name: str
    salary: str


e = Employee(123, 'Sivaram', '$100000')
e.salary = '$150000'
print(e)


# readonly dataclass
@dataclass(frozen=True)
class Employee1:
    id: int
    name: str
    salary: str


e1 = Employee1(123, 'Sivaram', '$100000')
# e1.salary = '$150000' # result in "FrozenInstanceError"
print(e)
