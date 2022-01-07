class A:

    def m1(self):
        print("Method of A")


class B(A):

    def m2(self):
        print("Method of B")


class C(A):

    def m2(self):
        print("Method of C")


class D(B, C):

    def m2(self):
        super().m2()


if __name__ == "__main__":
    d = D()
    d.m1()
    d.m2()
# When occurs a conflict with multiple methods from superclasses, Python uses the M.R.O (Method Resolution Order)
# which is a standardized behavior all classes implement to solve this problem.
# In our example, methods from B are called instead of C.
# It follows the inheritance order!
print(D.__mro__)
print(D.mro())
