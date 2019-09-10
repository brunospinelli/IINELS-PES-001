arquivo = open("multiplas-linhas.txt", "w")
linhasDoTexto = ["acertos Tempo Barra\n", "10 20 m esq\n", "10 20 m esq\n"]

arquivo.writelines(linhasDoTexto)
arquivo.close()

arquivo = open("multiplas-linhas.txt", "r")

for linha in arquivo:
    print(linha)
    
arquivo.close()
