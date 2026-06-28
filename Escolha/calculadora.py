import math

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Raiz")
operacao = int(input("Escolha a operação: "))

if operacao==5:
    x = int(input("Digite a base: "))
    y = int(input("Digite o expoente: "))
elif operacao==6:
    x = int(input("Digite o radicando: "))
    y = int(input("Digite o índice: "))
else:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))

match operacao:
    case 1:
        calc = x+y
        print(f"{calc}")
    case 2:
        calc = x-y
        print(f"{calc}")
    case 3: 
        calc = x*y
        print(f"{calc}")
    case 4:
        calc = x/y
        print(f"{calc}")
    case 5: 
        calc = x**y
        print(f"{calc}")
    case 6: 
        calc = x ** (1/y) 
        print(f"{calc}")