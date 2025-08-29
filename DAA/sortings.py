count = 0

def mergeSort(arr):
    global count
    if len(arr) > 1:
        count += 1
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            count += 1
            if L[i] <= R[j]:
                count += 1
                arr[k] = L[i]
                i += 1
            else:
                count += 1
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            count += 1
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            count += 1
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    global count
    for i in range(len(arr)):
        count += 1
        print(arr[i], end=" ")
    print()

arr = [12, 11, 13, 5, 6, 7]
print("Given array is")
printList(arr)
mergeSort(arr)
print("\nSorted array is ")
printList(arr)

print("Number of comparisons:", count)


count1 = 0

def quickSort(arr, low, high):
    global count1
    if low < high:
        count1 += 1
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    global count1
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        count1 += 1
        if arr[j] <= pivot:
            count1 += 1
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)

print("Given array is")
printList(arr)

quickSort(arr, 0, n - 1)

print("\nSorted array is ")
printList(arr)

print("Number of comparisons:", count1)

