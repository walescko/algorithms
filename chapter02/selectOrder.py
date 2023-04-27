def minorSearch(array01):
    minor = array01[0]
    indexMinor = 0
    for i in range(1, len(array01)):
        if array01[i] < minor:
            minor = array01[i]
            indexMinor = i
    return indexMinor


def SelectSearch(array):
    arrayNew = []
    for i in range(len(array)):
        minor = minorSearch(array)
        arrayNew.append(array.pop(minor))
    return arrayNew


print(SelectSearch([5, 43, 3, 99, 6, 2, 10, 1]))

