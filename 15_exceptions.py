# try...except
try:
    1 / 0
except (ZeroDivisionError, NameError) as se:
    print(f'Specific exception: {se}')
except Exception as e:
    print(f'General exception: {e}')

# try...except...else
try:
    print('hello')
except (ZeroDivisionError, NameError) as se:
    print(f'Specific exception: {se}')
except Exception as e:
    print(f'General exception: {e}')
else:  # Executed only when no exception occurs or no `break` statement is executed in the enclosing `try` block
    print('No exception')

# Raise exceptions
try:
    raise NameError('Invalid name')
    # raise NameError
except Exception as e:
    print(e)
    # raise  # Re-raise the same exception to the caller


# try...finally
def try_finally():
    try:
        raise KeyboardInterrupt
    except NameError:
        pass
    finally:
        print('Cleaning up after user interrupt')
        # return None  # `return` statement in `finally` clause suppresses return value from `try` clause and also re-raising the occurred exception


# try_finally()


# User defined exceptions
class UserDefinedError(Exception):  # Good to end with "Error" as a convention
    pass


# Exception chaining
def chain_exceptions():
    try:
        raise ValueError('Invalid value')
    except ValueError as ve:
        # raise Exception from ve  # `from` clause is to indicate that this exception is directly caused by above value exception
        raise Exception from None  # `None` will disable exception chaining i.e., only this exception will be raised and the above exception is suppressed
    except Exception as e:
        pass
        # raise Exception  # This exception will be attached to the above occurred exception during execution


# chain_exceptions()

# Grouping and raising multiple exceptions
def group_exceptions():
    try:
        raise ExceptionGroup('There were multiple exceptions',
                             [
                                 # This must be an exception instance not type like in the normal `raise NameError` case
                                 NameError('Wrong name'),
                                 ValueError('Wrong value')
                             ])
    except* NameError as e:  # `except*` is used to extract a specific type of exception from the exception group
        print(e)
    except* ValueError as e:
        print(e)


# group_exceptions()

# Nested group exceptions
def nest_group_exceptions():
    try:
        raise ExceptionGroup('group1',
                             [
                                 NameError('Wrong name1'),
                                 ValueError('Wrong value1'),
                                 ExceptionGroup(
                                     'group2',
                                     [
                                         NameError('Wrong name2'),
                                         ValueError('Wrong value2'),
                                         # Since this is not extracted using `except*`, it will be either caught by
                                         # general `Exception` clause or re-raised if there is no general clause like in this case
                                         ZeroDivisionError('x/0 error')
                                     ])]
                             )
    except* NameError as e:  # `except*` is used to extract a specific type of exception from the exception group
        print(e)
    except* ValueError as e:
        print(e)


# nest_group_exceptions()

# Exception notes is used to add some extra information to the caught exception
try:
    raise ValueError
except ValueError as e:
    e.add_note('Some info')
    e.add_note('Some more info')
    raise
