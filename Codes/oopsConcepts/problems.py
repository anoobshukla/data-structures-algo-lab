# add =lambda a,b:a+b
# print(add(5,6))

# evenNum = [x for x in range(1,11) if x%2 ==0]
# print("evenNum",evenNum)


# nums = [1, 2, 3, 4]
# even = list(filter(lambda x: x % 2 == 0, nums))
# print("even",even)


def square(x):
    return x * x
numbers = 1,2,3
squares = list(map(square, numbers))
print(squares)


arr = [2,2,2,3,3,4,5,5,5,]

freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1

print("freq",freq)
