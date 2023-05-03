def sum01(vector):
    if vector == []:
        return 0
    else:
        return vector[0] + sum01(vector[1:])

sum = 0
vector = [11, 12, 13]
print(len(vector))
print(sum01(vector))
