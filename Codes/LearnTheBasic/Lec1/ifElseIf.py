class Solution:
    def marksInput(self) -> int:
        StuMarks= int(input("Enter your Number:"))
        return StuMarks
    def studentGrade(self, marks:int) -> str:
        if marks >= 90:
            return("Grade A")
        elif marks >= 70 and marks <= 90:
            return("Grade B")
        elif marks >= 50 and marks <= 70:
            return("Grade C")
        elif marks >= 35 and marks <= 50:
            return("Grade D")
        else:
            return("Fail")

sol = Solution()
marks= sol.marksInput()
if marks <= 100:
    print(sol.studentGrade(marks))
else:
    print("Are you out of your mind!!")