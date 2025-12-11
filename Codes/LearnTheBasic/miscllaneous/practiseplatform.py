class PatternProblems:

    @staticmethod
    def square(n):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()

    @staticmethod
    def increasingTriangle(n):
        for i in range(n):
            for j in range(i + 1):
                print("*", end=" ")
            print()

    @staticmethod
    def decreasingTriangle(n):
        for i in range(n):
            for j in range(i, n):
                print("*", end=" ")
            print()


# ✅ Calling the functions
PatternProblems.square(5)
print()
PatternProblems.increasingTriangle(5)
print()
PatternProblems.decreasingTriangle(5)
