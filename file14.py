print("Olá, aqui calculamos o seu salário mensal")
valorhora = float(input("Insira o valor recebido por hora "))
horas = float(input("Insira o valor de horas trabalhadas: "))
salariob = valorhora * horas

impostoderenda = salariob * 0.11
inss = salariob *  0.08
sindicato = salariob * 0.05


salariol = salariob - impostoderenda - inss - sindicato

print("O seu salario bruto é de: R${}.".format(salariob))
print("O seu salario líquido é de: R${}.".format(salariol))
print("O desconto do Imposto de Renda é de: R${}.".format(impostoderenda))
print("O desconto do INSS é de: R${}.".format(inss))
print("O desconto do Sindicato é de: R${}.".format(sindicato))