# Author: Jet Semrick
# Date: 7-20-2022
# Problem: Given an unordered array consisting of consecutive integers without any duplicates find the min number of swaps to sort the array.

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

def isSorted(arr):
    for n in arr:
        if (arr.index(n) != 0):
            if arr[arr.index(n)-1] > arr[arr.index(n)]:
                return False
    return True

def minimumSwaps(arr):
    count = 0
    if (isSorted(arr)):
        return 0
    while (isSorted(arr) == False):
        for n in arr:
            if ((n - 1) != arr.index(n)):
                arr = swap(arr, arr.index(n), n-1)
                count += 1
    return count

# Tests
print("Test 1: ", minimumSwaps([4,3,1,2]) == 3)
print("Test 2: ", minimumSwaps([1,3,5,2,4,6,7]) == 3)
print("Test 3: ", minimumSwaps([20,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,1]) == 1)