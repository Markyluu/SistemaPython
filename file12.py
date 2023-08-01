altura = float(input("Insira sua altura (ex. 1.77): "))
genero = int(input("Qual seu genero? Digite 1 para feminino ou 2 para masculino : "))

feminino = (62.1*altura) - 44.7
masculino = (72.7*altura) - 58


if(genero == 1):
    print("O seu peso ideal é: {}".format(feminino))

elif(genero == 2):
    print("O seu peso ideal é: {}".format(masculino))
