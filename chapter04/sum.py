def sum01(vector):
    if vector == []:
        return vector[0]
    else:
        return vector[i] + sum01(vector[i+1])

sum = 0
vector = [11, 12]
print(len(vector))
print(sum01(vector))
