soma = 0

for i in range(1, 11):
    num = float(input(f"Digite o {i}º num: "))
    soma += num

media = soma / 10
print(f"A média aritmética dos valores é: {media}")