import math
capacidadelata = 18
capacidadeLitro = 3
precoLata = 80
areatotalLata = capacidadelata * capacidadeLitro

totalMetros = int(input("Insira a quantidade de metros a serem pintados: "))

totalLatas = math.ceil(totalMetros / areatotalLata)
totalPreco = totalLatas * precoLata

print("O total de latas a serem comprado é: {}, sendo o valor total: R${}.".format(totalLatas, totalPreco))
    