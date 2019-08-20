botao1Apertado = int(input("O rato apertou o botão 1?"))
botao2Apertado = int(input("O Rato apertou o botão 2?"))

if(not botao1Apertado and not botao2Apertado):
    print("Nenhuma comida foi adicionada")

if(botao1Apertado and not botao2Apertado):
    print("10mg foi adicionada")

if(not botao1Apertado and botao2Apertado):
    print("20mg foi adicionada")

if(botao1Apertado and botao2Apertado):
    print("40mg foi adicionada")

print("Fim de programa!!")

