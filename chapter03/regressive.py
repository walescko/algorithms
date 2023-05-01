def regressive(i):
    print(i)
    if i <= 1:  # base case
        return
    else:
        regressive(i - 1)  # recursion


print(regressive(4))
