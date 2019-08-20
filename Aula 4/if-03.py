strLazy        = input("\nVocê é uma pessoa preguiosa? ")

strIntelligent = input("Você é uma pessoa inteligente? ")

if(strLazy == "n" and strIntelligent == "n"):
    print("Você não é preguiçoso nem inteligente.\n")

if(strLazy == "n" and strIntelligent == "s"):
    print("Você não é preguiçoso, mas é inteligente.\n")

if(strLazy == "s" and strIntelligent == "n"):
    print("Você é preguiçoso, mas não é inteligente.\n")

if(strLazy == "s" and strIntelligent == "s"):
    print("Você é preguiçoso e inteligente.\n")

print("Fim do Programa.")