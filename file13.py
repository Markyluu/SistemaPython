pesototal = float(input("Insira o peso total: "))

excesso = pesototal - 50
multa = excesso * 4
if (pesototal > 50 ):
    print("O valor da multa será de: R${} devido ao excesso de {}kg".format(multa, excesso))

elif (pesototal <= 50):
    print("Você não possui multas pendentes, não há excesso de peso.")