# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def MyFunction(arg1, arg2, *, suppress_exc=False):
    pass


# try to call the function without the keyword
# myFunction(1, 2, True)
MyFunction(1, 2, suppress_exc=True)
