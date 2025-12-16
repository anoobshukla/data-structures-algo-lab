
# Inheritance is an OOP concept where a child (derived) class acquires properties and methods of a parent (base) class.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving")


c = Car("Toyota")
c.start()   # inherited method
c.drive()   # child’s own method


class A:
    def show(self):
        print("A.show")

class B(A):
    def show(self):
        print("B.show")

class C(A):
    def show(self):
        print("C.show")

class D(B,C):
    pass

d = D()
d.show()
print(D.mro())


