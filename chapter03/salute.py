def salute(name):
    print("Olá, " + name + "!")
    salute2(name)
    print("pra dizer adeus... pra dizer jamais...")
    byebye()

def salute2(name):
    print("Como vai " + name + "?")


def byebye():
    print("ok, tchau!")


print(salute("Maggie"))