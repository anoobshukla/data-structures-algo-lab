class Resource:
    lst = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    exceptionText = 'Are you insane!!'

class Solution:
    def dayInput(self) -> int:
        dayInt= int(input("Enter your Number:"))
        return dayInt
    def whichWeekDay(self, day:int) -> str:
        if 1 < day < 7 :
            return Resource.lst[day -1]    
        else:
            return Resource.exceptionText

sol = Solution()
print(sol.whichWeekDay(sol.dayInput()))