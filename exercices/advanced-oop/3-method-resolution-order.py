class A():
    num = 1

class B(A):
    pass

class C(A):
    num = 3

class D(B, C):
    pass

print(D.num)

# Python obeys the first method in the chain that defines num. The order followed
# is [D, B, C, A, object] where object is Python's base object class.
# In this example, the first class to define and/or override a previously defined
# num is C.
