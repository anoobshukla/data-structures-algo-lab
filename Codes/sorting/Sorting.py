class Sorting:
    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if arr[j] >= arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr
    
    def selectionSort(self,arr):
        n = len(arr)
        for i in range(n):
            minIdx = i
            for j in range(i+1,n):
                if arr[j] < arr[minIdx]:
                    minIdx = j
            arr[i], arr[minIdx] = arr[minIdx],arr[i]

        return arr
    
    def insertionSort(self,arr):
        n = len(arr)
        for i in range(n):
            key = arr[i]
            j = i-1
            while i > 0 and arr[j] > key :
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr


sol = Sorting()
print(sol.bubbleSort([4,5,3,4,6,7,8]))

print(sol.selectionSort([1,3,4,2,3,4]))

print(sol.insertionSort([1,3,4,2,3,4]))


