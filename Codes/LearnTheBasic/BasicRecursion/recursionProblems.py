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

    def printNum(self,n):
        if n == 1:
            return 1
        print(n, end = " ")
        return self.printNum(n-1)
    
    def ascPrintNum(self, i ,n):
        if i ==n :
            return n
        print(i,end = " ")
        return self.ascPrintNum(i+1,n)
        # print("i",i)

# Sum of first N numbers
    def sumFirstNum(self,n):
        if n <= 0:
            return 0
        return n + self.sumFirstNum(n-1)

#Reverse an Array
    def reverse(self,arr):
        return(arr[::-1])
    
    def recReverse(self,arr,left ,right):
        if left >= right :
            return
        arr[left],arr[right] = arr[right], arr[left]
        return self.recReverse(arr,left+1,right-1)

arr = [1,2,3,4,5]

fact = RecursionProblems("Cow")
# print(fact.factorial(3))
# print(fact.fib(6))
# print(fact.ascPrintNum(1,5))
# print("Sum ", fact.sumFirstNum(3))
fact.recReverse(arr, 0 ,len(arr)-1)
print("arr",arr)