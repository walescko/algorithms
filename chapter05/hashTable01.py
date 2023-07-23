voted = {}

def checkVoter(name):
    if voted.get(name):
        print('Mande embora, já votou')
    else:
        voted[name] = True
        print("Pode votar!")


print(voted)
checkVoter("Jonh")
print(voted)
checkVoter("Juliana")
print(voted)
checkVoter("Walescko")
print(voted)
checkVoter("Juliana")
print(voted)
checkVoter("Walescko")
