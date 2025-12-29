class striverArrayProblems:

    def largestElement(self,arr):
        n = len(arr)
        eleMax = arr[0]
        for i in range(n):
            if arr[i] > eleMax:
                eleMax = arr[i]
        return eleMax
    

# lst = [1,4,89,5,3,4,5,3,2,45,6,7]
# sol = striverArrayProblems()
# largestEllementArray = sol.largestElement(lst)
# print(largestEllementArray)

    def secondLargetsElement(self,arr):
        n = len(arr)
        max1 = max2 = float('-inf')
        for i in range(n):
            # print(arr[i],max1,max2)
            if arr[i] > max1:
                max1 = max2
                max2 = arr[i]
            elif arr[i] > max2 and arr[i] < max1:
                max2 = arr[i]
                
            
        return max1, max2


# lst = [1,4,9,5,3,4,5,3,2,5,6,7]
# sol = striverArrayProblems()
# maxTwoSum = sol.secondLargetsElement(lst)
# print(maxTwoSum)

    def secondSmallestElement(self,arr):
        n = len(arr)
        max1 = max2 = float('inf')
        for i in range(n):
            # print(arr[i],max1,max2)
            if arr[i] < max1:
                max1 = max2
                max2 = arr[i]
            elif arr[i] < max2 and arr[i] > max1:
                max2 = arr[i]
                
            
        return max1, max2


# lst = [1,4,9,5,3,4,5,3,2,5,6,7]
# sol = striverArrayProblems()
# maxTwoSum = sol.secondSmallestElement(lst)
# print(maxTwoSum)


    def maxTwoSum(self,arr):
        n = len(arr)
        maxSum = float('-inf')
        for i in range(n):
            for j in range(i+1,n):
                currSum = 0
                currSum = arr[i] + arr[j]
                maxSum = max(currSum,maxSum)
        return maxSum

# lst = [1,4,9,5,3,4,5,3,2,5,6,7]
# sol = striverArrayProblems()
# maxTwoSum = sol.maxTwoSum(lst)
# print(maxTwoSum)

    def twoSumBrute (self,arr,k):
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if arr[i] + arr[j] == k:
                    return i,j

    def twoSumOptimised(self,arr,k):
        seen = {}
        n = len(arr)
        for i, char in enumerate(arr):
            # seen[i] = char
            diff = k - char
            if diff in seen:
                return [seen[diff],i]
            seen[char] = i

# lst = [2,7,11,15]
# sol = striverArrayProblems()
# maxTwoSum = sol.twoSumOptimised(lst,9)
# print(maxTwoSum)
    def checkSorted(self,arr):
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
        return True

                
# lst = [1,2,3,4,5,6,8]
# sol = striverArrayProblems()
# maxTwoSum = sol.checkSorted(lst)
# print(maxTwoSum)

    def longestSubArrayBrute(self,arr,k):
        n = len(arr)
        maxLen = 0
        for i in range(n):
            currSum = 0
            for j in range(i,n):
                currSum+=arr[j]
                if currSum ==k :
                    maxLen = max(maxLen,j-i+1)
        return maxLen
    
# lst = [10, 5, 2, 7, 1, 9]
# k = 15
# sol = striverArrayProblems()
# maxTwoSum = sol.longestSubArrayBrute(lst,k)
# print(maxTwoSum)
    def duplSortedArr(self,arr):
        n = len(arr)
        arr2 = []
        for i in range(n-1):
            if arr[i] != arr[i+1] :
                arr2.append(arr[i])
            
        return arr2

# lst = [1,1,2,2,3,4,5,6]
# k = 15
# sol = striverArrayProblems()
# maxTwoSum = sol.duplSortedArr(lst)
# print(maxTwoSum)

    def rotateArrOnePlace(self,arr):
        if len(arr) <=1:
            return arr
        first = arr[0]
        n = len(arr)
        for i in range(1,n):
            arr[i-1] = arr[i]
        arr[-1] = first
        return arr


# lst = [1,2,3,4,5,6,7,8]
# k = 15
# sol = striverArrayProblems()
# maxTwoSum = sol.rotateArrOnePlace(lst)
# print(maxTwoSum)


    def rotateByKPlace(self,arr,k):
        n = len(arr)
        if k > n : 
            return arr
        arr2 = arr[k:n]
        arr3 = arr[:k]
        arr4 = arr2 + arr3
        return arr4
    
    def rotateArrKPlaceBrute(self,arr,k):
        if len(arr) <=1:
            return arr
        # first = arr[0]
        n = len(arr)
        for _ in range(k):
            first = arr[0]
            print(arr)
            for i in range(1,n):
                arr[i-1] = arr[i]
            arr[-1] = first
        return arr
    
# lst = [1,2,3,4,5,6,7,8]
# k = 15
# sol = striverArrayProblems()
# maxTwoSum = sol.rotateArrKPlaceBrute(lst,4)
# print(maxTwoSum)    

    def moveZeroToEndBrute(self,arr):
        n = len(arr)
        cnt = 0
        print("length",n)
        for i in range(n):
            for j in range(i,n-1):
                print("i and j", i,j,arr[i], arr[j])
                if arr[j] == 0:
                    arr[j] = arr[j+1]
                    arr[j+1] = 0
                    cnt +=1
        return arr,cnt
    
    def moveZeroes(self,arr):
        j = 0
        n= len(arr)
        for i in range(n):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j],arr[i]
                j+=1
        return arr


# lst = [1,2,0,3,0]
# k = 15
# sol = striverArrayProblems()
# maxTwoSum = sol.moveZeroes(lst)
# print(maxTwoSum)   
#  
    def linSearch(self,arr,k):
        n = len(arr)
        for i in range(n):
            if arr[i] == k:
                return i    
        return -1
# lst = [1,2,3,4,5,6]
# k = 3
# sol = striverArrayProblems()
# maxTwoSum = sol.linSearch(lst,k)
# print(maxTwoSum) 

    def missingNumber(self, arr,n):
        # n= len(arr)
        for i in range(n-1):
            print(arr[i])
            if arr[i+1] - arr[i] != 1:
                num = (arr[i+1] + arr[i])//2
                return num
# lst = [1,2,3,4,5,7,8,9,]
# k = 5
# sol = striverArrayProblems()
# maxTwoSum = sol.missingNumber(lst,k)
# print(maxTwoSum) 

    def maxConseOnesBrute(self,arr,k):
        result = 0
        n= len(arr)
        for i in range(n):
            cnt = 0
            for j in range(i,n):
                if arr[j] == 0:
                    arr[j]= 1
                    cnt+=1
                if cnt >k:
                    break
                result = max(result,j-i+1)
        return result

# lst = [1,0,1,1,0,1,1,0]
# k = 2
# sol = striverArrayProblems()
# maxTwoSum = sol.maxConseOnesBrute(lst,k)
# print(maxTwoSum) 

    def onceTwice(self,arr):
        n = len(arr)
        seen = {}
        for value in arr:
            if value in seen:
                seen[value]+=1
            else:
                seen[value] = 1


        for value, cnt in seen.items():
            if cnt == 1 :
                return value
        return -1

# lst = [4,1,2,1,2]
# sol = striverArrayProblems()
# maxTwoSum = sol.onceTwice(lst)
# print(maxTwoSum)

    def subArraySumBrute(self,arr,target):
        arr2 = []
        n = len(arr)
        count  = 0 
        maxLen = 0
        for i in range(n):
            currSum = 0
            for j in range(i,n):
                currSum += arr[j]
                if currSum == target:

                    arr2.append(arr[i:j+1])
                    # print(arr2)
                    count+=1
                    maxLen = max(maxLen, j-i+1)
        return arr2,maxLen 
    

# lst = [4,1,2,1,2]
# sol = striverArrayProblems()
# k = 5
# maxTwoSum = sol.subArraySumBrute(lst,k)
# print(maxTwoSum)
