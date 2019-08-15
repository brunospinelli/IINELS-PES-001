'''
Calculo do IMC
imc = (peso)/(altura)^2

Muito abaixo do peso
imc <= 17.0

Peso abaixo do normal
17.0 < imc <= 18.5

Peso normal
18.5 < imc <= 25.0

Acima do peso normal
25.0 < imc <= 30.0

Muito acima do peso
imc > 30.0

'''
# Calcula o IMC, dado um peso (Kg) e uma altura (m), e retorna o valor do IMC
def calcula_imc(peso, altura):
  imc = (peso/(altura)**2)
  return(imc)

# Retorna True ou False para a condição de: Muito abaixo do peso
def muito_abaixo_do_peso(imc):
    print("Muito baixo do peso normal:")
    return(imc <= 17.0)

# Retorna True ou False para a condição de: Abaixo do peso
def abaixo_do_peso(imc):
    print("Abaixo do peso normal:")
    return(imc > 17.0 and imc <= 18.5)

# Retorna True ou False para a condição de: Peso normal
def peso_normal(imc):
    print("Peso normal:")
    return(imc > 18.5 and imc <= 25.0)

# Retorna True ou False para a condição de: Acima do peso
def acima_do_peso(imc):
    print("Acima do peso normal:")
    return(imc > 25.0 and imc <= 30)

# Retorna True ou False para a condição de: Muito acima do peso
def muito_acima_do_peso(imc):
    print("Muito acima do peso normal:")
    return(imc > 30)

# Recebe a altura e o peso
peso = float(input("Digite o peso (Kg):"))
altura = float(input("Digite a altura (m):"))

# Printa o IMC
imc = calcula_imc(peso, altura)
print("Valor do IMC:")
print(imc)

# Printa as condições 
print(muito_abaixo_do_peso(imc))
print(abaixo_do_peso(imc))
print(peso_normal(imc))
print(acima_do_peso(imc))
print(muito_acima_do_peso(imc))