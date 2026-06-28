peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))

imc = peso/(alt ** 2)

print(f"IMC: {imc:.2f}")