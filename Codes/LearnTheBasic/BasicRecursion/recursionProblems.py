class RecursionProblems:
    def __init__(self, name):
        self.name = name

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def fib(self,n):
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)


fact = RecursionProblems("Cow")
print(fact.factorial(3))
print(fact.fib(6))
