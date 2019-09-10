arquivo = open("bruno.txt", "w")

print(arquivo)

arquivo.write("Eu sou eu \n")
arquivo.write("Eu sou eu \n")
arquivo.write("Eu sou eu \n")
arquivo.write("Eu sou eu \n")

arquivo.close()
arquivo = open("bruno.txt", "r")

print(arquivo.read())
