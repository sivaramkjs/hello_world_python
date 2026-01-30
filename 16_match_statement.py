def http_error(status):
    match status:
        case 401:
            return 'Unauthorized'
        case 403:
            return 'Forbidden'
        case 500:
            return 'Internal Server Error'
        case 200 | 201 | 202:  # or pattern
            return 'success'
        case (301 | 302 | 304) as code:  # sub-pattern capture into a variable
            return code
        case _:
            return 'Unknown error'


print(http_error(401))
print(http_error(501))
print(http_error(301))


# sequence pattern matching
def check_point(point):  # point is an (x,y) tuple
    match point:
        case (0, 0):
            return f'Origin'
        case (x, 0):
            return f'{point} x= {x}'
        case (0, y):
            return f'{point} y= {y}'
        case (x, y):
            return f'{point} x= {x}, y= {y}'
        case _:
            return 'Not a point'


print(check_point((0, 0)))
print(check_point((5, 0)))
print(check_point((5, 4)))
print(check_point(501))


# class instance pattern matching
class Point:
    # Using "__match_args__" special attribute in class to use positional arguments in pattern matching
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_point_cls(point):  # point is an (x,y) tuple
    match point:
        case Point(x=0, y=0):  # Explicit keyword arguments for pattern matching
            return f'Origin'
        case Point(1, 2):  # Implicit positional arguments for pattern matching leveraging "__match_args__" attribute
            return f'(1, 2)'
        case Point(x=x, y=0):
            return f'x= {x}'
        case Point(x=0, y=y):
            return f'y= {y}'
        case Point():
            return f'Some point'
        case _:
            return 'Not a point'


print(check_point_cls(Point(0, 0)))
print(check_point_cls(Point(1, 2)))
print(check_point_cls(Point(y=2, x=1)))
print(check_point_cls(Point(5, 0)))
print(check_point_cls(Point(5, 4)))
print(check_point_cls(501))


# Pattern matching with guards ("if" clause)
def check_point_cls_guard(point):  # point is an (x,y) tuple
    match point:
        case Point(x=0, y=0):  # Explicit keyword arguments for pattern matching
            return f'Origin'
        case Point(x, y) if x == y:
            return f'({x}, {y})'
        case _:
            return 'Some point'


print(check_point_cls_guard(Point(0, 0)))
print(check_point_cls_guard(Point(1, 2)))
print(check_point_cls_guard(Point(1, 1)))


# Truthy/Falsy values pattern matching
def check_bool_val(value):
    match value:
        case True:  # Matches only the literal singleton "True" value by identity
            print("True")
        case False:  # Matches only the literal singleton "False" value
            print("True")
        case None:  # Matches only the literal singleton "None" value
            print("True")
        case x if x:  # Matches any Truthy value by equality
            print("Truthy")
        case x if not x:  # Matches any Falsy value by equality
            print("Falsy")
        case _:
            print("Other")


check_bool_val(True)
check_bool_val(False)
check_bool_val(None)
check_bool_val("")
check_bool_val(1)


# Matching built-in classes
def check_val(value):
    match value:
        case str(val):  # Combining built-in class validation matching and variable capture
            # case str() as val:
            print(f'{val} is string')
        case int(val):
            print(f'{val} is int')
        case bool(val):
            print(f'{val} is bool')
        case _:
            print(f'Other data type')


check_val('hello')
check_val(123)
check_val(True)
check_val([])
