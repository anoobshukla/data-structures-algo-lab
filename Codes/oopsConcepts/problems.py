import asyncio

# add =lambda a,b:a+b
# print(add(5,6))

# evenNum = [x for x in range(1,11) if x%2 ==0]
# print("evenNum",evenNum)


# nums = [1, 2, 3, 4]
# even = list(filter(lambda x: x % 2 == 0, nums))
# print("even",even)


# def square(x):
#     return x * x
# numbers = 1,2,3
# squares = list(map(square, numbers))
# print(squares)


# arr = [2,2,2,3,3,4,5,5,5,]

# freq = {}
# print(freq)
# for i in arr:
#     print("i",i)
#     freq[i] = freq.get(i, 0) + 1

# print("freq",freq)


# class Solution:
#     def maxSubArray(self, nums):
#         subArr = 0
#         n = len(nums)
#         for i in range(n):
#             currSum = 0
#             for j in range(i,n):
#                 currSum += nums[j]
#                 # print("currSum",currSum)
#                 subArr = max(currSum,subArr)
#         return subArr
# sol = Solution()
# print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


# print(float("_inf"))

# max_sum = float('-inf')
# print(max_sum)
#     def countOddEven(self,arr):
#         evenCount = 0
#         oddCount = 0 
#         for i in arr:
#             if i%2 == 0 :
#                 evenCount += 1
#             else:
#                 oddCount +=1 
#         return evenCount , oddCount

# sol = Solution()
# print(sol.countOddEven([1,2,3,4,5,6,7,8,9]))


# def twoSum(nums, target):
#     seen = {}  # value -> index
#     for i, num in enumerate(nums):
#         rem = target - num
#         print("rem",rem)
#         seen[num] = i

#         if rem in seen:
#             return [seen[rem], i]
#         # seen[num] = i
#         print("seen In loop",seen)

# nums = [2, 11,3,6, 15]
# target = 9

# print(twoSum(nums,target))


# async def fetchData():
#     print("Fetching Data")
#     await asyncio.sleep(1)
#     print("Data Fetched")

# asyncio.run(fetchData())

# arr = [3,4,1,2,7,0,9,8]

# # arr = [4,3,4,5,6,7,5,3,2,1]
# m1 = float('-inf')
# m2 = float('-inf')
# for x in arr:
#     if x > m1 :
#         m2 = m1
#         m1 = x
#     elif x > m2 :
#         m2 = x


# print("minimum2",m2,m1)



# arr = [1,1,2,2,4,4,5,5,6,6,7]

# arr2 = []
# n = len(arr)
# for i in range(n-1):
#     print("i",i)
#     print("qwer",arr[i])
#     if arr[i] != arr[i+1]:
#         arr2.append(arr[i])
# arr2.append(arr[-1])
# print(arr2)



# arr = [1,2,3,4,5]
# # arr2 = []

# n = len(arr)
# k = 3

# arr2 = arr[k:n] + arr[0:k]
# # for i in range(k,n):
# #     arr2.append(arr[i])
# # for j in range(0,k):
# #     arr2.append(arr[j])
# print(arr2)

# arr = [1,0,3,4,3,2,0,3,4,9]
# arr2 = []
# n = len(arr)
# cnt = 0
# print("n",n)
# for i in range(n):
#     if arr[i] != 0:
#         arr2.append(arr[i])
#     else:
#         cnt+=1
#     # print("i",i)
#     # arr.pop(i)
# print(cnt)
# arr3 = arr2 + cnt * [0]
# print(arr3)


# nums = [1,2,3,4,5,6]
# totSum = 5
# left = 0
# right = len(nums) -1
# print(nums[right])
# print(nums[left])
# while left < right:
#     csum = nums[left] + nums[right] 
#     print("sum",csum)

#     if csum == totSum: 
#         print(left,right)
#         break
#     elif csum > totSum: 
#         right -=1 
#         print("inside sum is greater condition", right)
#     else:
#         print("inside sum is lesser condition", left)
#         left+=1
# else:
#     print("no pair found")

# class calculator:
#     def addition(self,a,b):
#         sum = a+b
#         return sum
    
#     def sub(self,a,b):
#         subs = a-b
#         return
    
#     def addition(self,a,b,c):
#         sum = a+b+c
#         return sum

# num = [1,2,3,4,3,2,1]
# # arr.split(num)
# text = 'madamas',
# def isPallindrome(num):
#     left = 0
#     right = len(num)-1
#     while left < right:
#         if num[left] == num[right]:
#             left+=1
#             right-=1
#             return True
#         else:
#             return False


# print(isPallindrome(text))



arr = [9,4,20,3,10,5 ]
target = 33

def subArraySumBrute(arr,target):
    arr2 = []
    n = len(arr)
    count  = 0 
    for i in range(n):
        currSum = 0
        for j in range(i,n):
            currSum += arr[j]
            if currSum == target:
                arr2.append(arr[i:j+1])
                # print(arr2)
                count+=1
    return arr2,count        

# result, count = subArraySumBrute(arr,33)
# print("subArrays",result)
# print("count",count)




nums = [0,1,1,0,1,0,0,1,1,1,1]
k = 2

def longestOnesBrute(nums,k):
    n = len(nums)
    result = 0

    for i in range(n):
        currSum = 0
        for j in range(i,n):
            if nums[j] == 0 :
                currSum+=1
            if currSum > k:
                break
            result = max(result,j-i+1)
    return result

print(longestOnesBrute(nums,2))
# left = 0
# right = len(nums) 
# while left<right:
#     if nums[left] == 0:
#         len
# def maxbinArr(nums,k):
#     currSum = 0
#     arr2 = []
#     for i in nums:
#         if i == 0:
#             currSum = 0
#         currSum+=i
#         arr2.append(currSum)
#     return arr2
#     # for i in arr2:
# print(maxbinArr(nums,k))