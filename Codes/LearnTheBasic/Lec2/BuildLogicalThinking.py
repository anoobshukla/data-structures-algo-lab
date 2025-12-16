class Patterns:

    def __init__(self, name):
        self.name = name

    def square(self,n):
        for i in range(n):
            for j in range(n):
                print("*", end = "")
            print()

    def triangle(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*", end = "")
            print()

    def inverseTriangle(self,n):
        for i in range(n):
            for j in range(i+1):
                print(" ", end = "")
            for j in range(n-i):
                print("*", end = "")
            for j in range(n-i):
                print("*", end = "")
            print()
        
        for i in range(n):
            for j in range(n-i):
                print(" ", end = "")
            for j in range(i+1):
                print("*", end = "")
            for j in range(i+1):
                print("*", end = "")
            print()
name = Patterns('name')
# name.square(5)
# name.triangle(5)
name.inverseTriangle(5)