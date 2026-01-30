# "namespace" is a logical mapping of names belonging to an object (e.g., module, class, function)
#
# There are 3 to 4 types of scopes (L(local) E(enclosing) G(global) B(builtins)
#   local: innermost scope (of a function)
#   non-local (in case of a nested function): enclosing function scope
#   module global: current module's scope
#   global: outermost scope containing built-in names

def scope_test():
    def set_local():
        spam = "local spam"  # Binds to "spam" in the local scope of this nested function

    def set_nonlocal():
        nonlocal spam  # Binds to "spam" in the enclosing function scope
        spam = "nonlocal spam"

    def set_global():
        # Binds to "spam" in the current module's global scope. Creates a new "spam" variable in the
        # global scope if it doesn't exist
        global spam
        spam = "global spam"

    spam = 'test spam'
    set_local()
    print('After local assignment:', spam)

    set_nonlocal()
    print('After nonlocal assignment:', spam)

    set_global()
    print('After global assignment:', spam)


scope_test()
print('In global scope:', spam)
