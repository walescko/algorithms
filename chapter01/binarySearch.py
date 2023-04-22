def binarySearch(listCall, item):
    down = 0
    upper = len(listCall) - 1
    while down <= upper:
        mid = int((down + upper) / 2)
        kik = listCall[mid]
        if kik == item:
            return mid
        if kik > item:
            upper = mid - 1
        else:
            down = mid + 1
    return None
myList = [1, 3, 5, 7, 9]
print(myList)
print(binarySearch(myList, 3))
print(binarySearch(myList, -1))
print("Hello")
