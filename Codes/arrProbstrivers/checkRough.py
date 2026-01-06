class Solution:
    def __init__(self,aname,aage,astandard) -> None:
        self.name = aname
        self.age = aage
        self.standard = astandard
    def twoSum(self,a,b):
        return a+b
    
    def printDetails(self):
        return f"Name is {self.name}, Age is {self.age}, and studies in {self.standard}"

# sol = Solution()


rohan = Solution("Rahul",28,9)
# sohan = Solution()
# mohan = Solution()

# rohan.name = "Rohan"
# rohan.age = 23
# rohan.standard = 11


# sohan.name = "sohan"
# sohan.age = 28
# sohan.standard = 11


# mohan.name = "Mohan"
# mohan.age = 24
# mohan.standard = 11



print(rohan.printDetails())

import random

# Step 1: Generate 100 even numbers
even_numbers = [x for x in range(201) if x%2 ==0]
print("evenNumbers",even_numbers)

# Step 2: Shuffle using Fisher–Yates
def shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        print("i", i)
        j = random.randint(0, i)
        print("i and j",i,j)
        print("arr[i] and arr[j]", arr[i], arr[j])
        arr[i], arr[j] = arr[j], arr[i]

shuffle(even_numbers)

print(even_numbers)