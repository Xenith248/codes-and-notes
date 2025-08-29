count = 0

def linearSearch(array, n, x):
    global count 
    for i in range(0, n):
        count += 1
        if array[i] == x:
            return i
    return -1

array = [2, 4, 0, 1, 9,6,7,3,11,17]
x = 2
n = len(array)
result = linearSearch(array, n, x)
if result == -1:
    count += 1
    print("Element not found")
else:
    count += 1
    print("Element found at index:", result)

print("Number of comparisons in linear search:", count)

count1 = 0

def binarySearch(arr, l, r, x):
    global count1 
    while l <= r:
        count1 += 1
        mid = l + (r - l) // 2
        if arr[mid] == x:
            count1 += 1
            return mid
        elif arr[mid] < x:
            count1 += 1
            l = mid + 1
        else:
            count1 += 1
            r = mid - 1
    return -1

arr = [0,1,2,3,4,6,7,9,11,17]
x = 2
n = len(arr)
result = binarySearch(arr, 0, n-1, x)
if result == -1:
    count1 += 1
    print("Element not found")
else:
    count1 += 1
    print("Element found at index:", result)

print("Number of comparisons in binary search:", count1)
