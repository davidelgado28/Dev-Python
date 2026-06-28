num = int(input("Digite um número: "))

print(f"=====Tabuada do {num}=====")

for i in range(1,11):
    calc = num*i
    print(f"{num} x {i} = {calc}") 