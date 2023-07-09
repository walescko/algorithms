def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        minors = [i for i in array[1:] if i <= pivot]
        biggers = [i for i in array[1:] if i > pivot]
        return quicksort(minors) + [pivot] + quicksort(biggers)

print(quicksort([10, 5, 2, 3]))