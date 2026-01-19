class A:
    def greet(self): print("Hello từ A")

class B(A):
    def greet(self): print("Hello từ B")

class C(A):
    def greet(self): print("Hello từ C")

class D( B, C ):
    pass

d = D()

d.greet()

print(D.__mro__)