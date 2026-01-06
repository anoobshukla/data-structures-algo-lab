from typing import List

class StriverBinaryProblems:
    def findTarget(self,arr,target):
        start = 0
        end = len(arr) -1 
        while start <= end :
            print("start, end", start, end)
            mid = (start + end) // 2
            print("mid", mid)
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                print("arr[mid]",arr[mid])

                start = mid + 1
            else :
                end = mid - 1
        return -1
# arr = [0,2,3,4,5,6,9,11]
# target = 2
# sol = StriverBinaryProblems()

# result = sol.findTarget(arr,target)
# print("result",result)

 
    def lowerBoundBrute(self,arr, k):
        n =len(arr)
        for i in range(n):
            if arr[i] <=k :
                lBound = arr[i-1]
                
        return lBound
    

    def lowerBoundOptimised(self,arr, k):
        n =len(arr)
        result = arr[n-1]
        left = 0
        right = n-1
        while left < right :
            mid = left + (right - left)//2
            if arr[mid] <= k : 
                result = mid
                left = mid +1
            else:
                right = mid -1
        return result


    
# arr = [0,1,2,3,4,5,6,9,11]
# target = 3
# sol = StriverBinaryProblems()

# result = sol.lowerBoundOptimised(arr,target)
# print("result",result)

    def upperBoundBrute(self,arr, k):
        n =len(arr) -1
        for i in range(n):
            print("i",i)
            if arr[i] <=k :
                lBound = arr[i+1]
                
        return lBound
    
    def upperBoundOptimised(self,arr, k):
        n =len(arr)
        result = arr[n-1]
        left = 0
        right = n-1
        while left < right :
            mid = left + (right - left)//2
            if arr[mid] <= k : 
                result = mid +2
                left = mid +1
            else:
                right = mid -1
        return result

# arr = [0,1,2,3,4,5,6,9,11]
# target = 5
# sol = StriverBinaryProblems()

# result = sol.upperBoundOptimised(arr,target)
# print("result",result)

    def searchInsertPosition(self, arr, target):
        n = len(arr)
        for i in range(n):
            if arr[i] == target:
                return i

# arr = [0,1,2,3,4,5,6,9,11]
# target = 5
# sol = StriverBinaryProblems()

# result = sol.searchInsertPosition(arr,target)
# print("result",result)

    def searchIndexPositionOptimised(self,arr, target):
        n = len(arr)
        left = 0
        right = n-1 
        while left <= right:
            mid = left + (right -left)//2
            print("mid",mid)
            if arr[mid] == target:
                return mid
            elif arr[mid] < target :
                left = mid +1
            else:
                right = mid -1
        return -1

# arr = [0,1,2,3,4,5,6,9,11]
# target = 9
# sol = StriverBinaryProblems()

# result = sol.searchIndexPositionOptimised(arr,target)
# print("result",result)

    def floorCeil(self,arr,target):
        left = 0
        right = len(arr) -1
        floor = arr[0]
        ceil = arr[right]
        while left < right:
            mid = left + (right -left)//2
            if arr[mid] == target:
                return arr[mid],arr[mid]
            elif arr[mid]< target:
                floor = arr[mid]
                left = mid +1
            else:
                ceil = arr[mid]
                right = mid -1
        return floor, ceil 

# arr = [0,1,2,3,4,5,6,9,11]
# target = 7
# sol = StriverBinaryProblems()

# result = sol.floorCeil(arr,target)
# print("result",result)

    def lastOccurenceBrute(self,arr,target):
        n = len(arr)
        lastOccur = -1
        firstOccur = -1

        for i in range(n):
            if arr[i] == target:
                if firstOccur == -1:
                    firstOccur = i
                lastOccur = i
                # break
        return lastOccur,firstOccur
    
# arr = [0,1,2,3,4,4,6,9,11]
# target = 4
# sol = StriverBinaryProblems()

# result = sol.lastOccurenceBrute (arr,target)
# print("result",result)

    def lastOccurenceOptimised(self, arr, target):
        left = 0
        right = len(arr)-1
        ans = -1
        while left < right :
            mid = left + (right -left)//2
            if arr[mid] == target:
                ans = mid
                left = mid+1
            if arr[left] <= target:
                left = mid +1
            else:
                right = mid -1
        return ans

# arr = [0,1,2,3,4,4,6,9,11]
# target = 4
# sol = StriverBinaryProblems()

# result = sol.lastOccurenceOptimised (arr,target)
# print("result",result)


    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high -low)//2
            if nums[mid] == target:
                return mid
            if nums[low] == nums[high] == nums[mid]:
                low = low +1
                high = high -1
                continue
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if nums[low] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

# arr = [0,1,2,3,4,4,6,9,11]
# target = 9
# sol = StriverBinaryProblems()

# result = sol.search (arr,target)
# print("result",result)

    def peakElement(self, arr):
        for i in range(len(arr)):
            if arr[i-1] <=arr[i] >= arr[i+1]:
                return i
            

# arr = [1,2,3,4,5,6,7,8,5,1]
# target = 9
# sol = StriverBinaryProblems()

# result = sol.peakElement (arr)
# print("result",result)


    def singleNumber(self,arr):
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] =1
        print(freq)
        # return freq
        for num, cnt in freq.items():
            if cnt == 1:
                return num
        

# arr = [11,11,22,33,33,44,44,55,55]
# target = 9
# sol = StriverBinaryProblems()
 
# result = sol.singleNumber (arr)
# print("result",result)


    def countOccurence(self, arr,target):
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        # print(freq)
        return freq[target]
 
# arr = [2, 2 , 3 , 3 , 3 , 3 , 4]
# target = 3
# sol = StriverBinaryProblems()
# result = sol.countOccurence(arr,target)

# print(result)

    def sqrt(self, num):
        ans =1
        for i in range(num):
            if i * i <= num:
                ans = i
                continue
            else:
                break
        return i -1

target = 38
sol = StriverBinaryProblems()
result = sol.sqrt(target)

print(result)