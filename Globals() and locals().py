#globals()
#locals()
#!/usr/bin/python3
from pprint import pprint
a=10
b=20
def foo():
    x=30 #x, and y are local variables
    y-40
print("locals()={0}".format(locals()))
print(locals()) #same as calling globals()
print('*',*80)
print("locals() == globals? ", locals() == globals())
print('*',*80)
foo()
# "globals()" returns a dict
# with all global variables
# in the current scope:

>>> globals()
{...}

# "locals()" does the same
# but for all local variables
# in the current scope:

>>> locals()
{...}
