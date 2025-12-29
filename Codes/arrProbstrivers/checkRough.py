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