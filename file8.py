print("Olá, aqui calculamos o seu salário mensal")
valorhora = float(input("Insira o valor recebido por hora "))
horas = float(input("Insira o valor de horas trabalhadas: "))

salario = valorhora * horas

print("O seu salário será de R${}.".format(salario))