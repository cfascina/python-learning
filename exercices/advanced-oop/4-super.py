class A():
    def truth(self):
        return "class A(): The number is even."

class B(A):
    pass

class C(A):
    def truth(self):
        return "class C(): The number is odd."

class D(B, C):
    def truth(self, num):
        if num % 2 == 0:
            return A.truth(self)
        else:
            return super().truth()

d = D()
print(d.truth(6))
print(d.truth(5))
