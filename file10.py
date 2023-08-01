num1 = int(input("Insira seu primeiro número inteiro: "))
num2 = int(input("Insira seu segundo número inteiro: "))
numreal = float(input("Insira seu número real: "))

produto = (num1 * 2) * (num2 / 2)
soma = (num1 * 3) + numreal
elevado = (numreal)**3

print("O resultado é: {}, {}, {}".format(produto, soma, elevado))