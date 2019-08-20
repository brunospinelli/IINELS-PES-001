'''
Calculo do IMC:
imc = (peso)/(altura)^2

Muito abaixo do peso:
imc <= 17.0

Peso abaixo do normal:
17.0 < imc <= 18.5

Peso normal:
18.5 < imc <= 25.0

Acima do peso normal:
25.0 < imc <= 30.0

Muito acima do peso:
imc > 30.0

'''

# Calcula o IMC, dado um peso (Kg) e uma altura (m), e retorna o valor do IMC.
def calcula_imc(peso, altura):
  imc = (peso/(altura)**2)
  return(imc)

#Retorna a condição do usuário.
def condicao(imc):
    if(imc <= 17.0):
        print("Muito abaixo do peso normal.\n")

    elif(imc > 17.0 and imc <= 18.5):
        print("Abaixo do peso normal.\n")

    elif(imc > 18.5 and imc <=25.0):
        print("Peso normal.\n")

    elif(imc > 25.0 and imc <=30):
        print("Acima do peso.\n")

    else:
        print("Muito acima do peso.\n")

    

# Recebe a altura e o peso.
peso = float(input("\nDigite o peso (Kg): "))
altura = float(input("Digite a altura (m): "))

# Printa o IMC.
imc = calcula_imc(peso, altura)
print("\nValor do IMC:")
print(imc)

# Printa a condição. 
print("\nCondição:")
condicao(imc)