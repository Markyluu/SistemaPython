import math
capacidadelataG = 18
capacidadelataP = 3.6
capacidadeLitro = 6
precoLataG = 80
precoLataP = 25 
areatotalLataG = capacidadelataG * capacidadeLitro
areatotalLataP = capacidadelataP * capacidadeLitro

totalMetros = int(input("Insira a quantidade de metros a serem pintados: "))

totalLatasG = math.ceil(totalMetros / areatotalLataG)
totalLatasP = math.ceil(totalMetros / areatotalLataP)
totalPrecoG = totalLatasG * precoLataG
totalPrecoP = totalLatasP * precoLataP

print("O total de latas grandes é: {}, sendo o valor total: R${}.".format(totalLatasG, totalPrecoG))
print("O total de latas pequenas é: {}, sendo o valor total: R${}.".format(totalLatasP, totalPrecoP))