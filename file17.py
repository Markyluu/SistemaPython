tamanho = float(input("Insira o tamanho do arquivo para download (em MB): "))
velocidade = float(input("Insira a sua velocidade de internet (em Mbps): "))

tempo = tamanho / velocidade


if (tempo <= 60 ):
    print("O dowload irá levar: {} segundos".format(tempo))

elif (tempo > 60 and tempo <= 3600):
    tempoM = int(tempo/60)
    print("O dowload irá levar aproximadamente: {} minutos".format(tempoM))

elif (tempo > 3600):
    tempoH = round(tempo/3600, 2)
    print("O dowload irá levar aproximadamente: {} horas".format(tempoH))