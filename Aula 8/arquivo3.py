arquivo = open("multiplas-linhas2.txt", "w")
linhasDoTexto = ["acertos Tempo Barra\n", "10 20 m esq\n", "10 20 m esq\n"]

arquivo.writelines(linhasDoTexto)
arquivo.close()

arquivo = open("multiplas-linhas2.txt", "r")

for linha in arquivo:
    word = linha.split()
    print(word)

    
arquivo.close()
