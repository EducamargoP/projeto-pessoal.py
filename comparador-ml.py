print("bem-vindo ao analisador de gastos!")
print("começando com bebidas ")
print("-------------------------------------------------------------------")


nome = str(input("diga o nome da cerveja ?"))
nome2 = float(input("diga quantos ml essa cerveja tem ?"))
numero = float(input("quantas unidades tem na caixa?"))
numero3 = float(input("quanto está o valor da unidade ?R$:"))


valor = nome2 * numero /1000
valor2 = numero3 * numero

print("-----------------------------------------------------------------")

cerveja = str(input("diga o nome da cerveja ?"))
cerveja2 = float(input("diga quantos ml essa cerveja tem ?"))
num = float(input("quantas unidades tem na caixa?"))
num3 = float(input("quanto está o valor da unidade ?R$:"))
conta = cerveja2 * num / 1000
conta2 = num3 * num


print("-------------------------------------------------------------------")

print("comparando as 2 marcas . . . ")
print("\033[1;33;40m a cerveja {}  contém {:2.2f} litros com um valor de R$: {:2.2f}  na caixa \033[m".format(nome,valor,valor2))

print("\033[1;33;40m a cerveja {}  contém {:2.2f} litros com um valor de R$: {:2.2f}  na caixa \033[m".format(cerveja,conta,conta2))

print("-------------------------------------------------------------------")

pessoas = float(input("Informe o numero de convidados ?"))

calculo = pessoas * 4
calculo1 = valor2 / 4
calculo2 = conta2 / 4
soma = calculo1 * calculo
soma2 = calculo2 * calculo

print("Para um melhor atendimento aos convidados iremos trablhar com 4l por pessoa")
print(" voce irá comprar {} litros ".format(calculo))
print("\033[1;33;40m na cerveja {} de {} ml ira gastar R$:{:.2f}\033[m".format(nome,nome2,soma))
print("\033[1;33;40m na cerveja {} de {} ml ira gastar R$:{:.2f}\033[m".format(cerveja,cerveja2,soma2))

print("-------------------------------------------------------------------")

if conta2 < valor2:
    print(" a cerveja ganhadora foi  {} de {} ml ".format(cerveja,cerveja2))
else:
    print(" a cerveja ganhadora foi  {} de {} ml ".format(nome,nome2))

print("-------------------------------------------------------------------")