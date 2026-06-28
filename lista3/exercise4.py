time1 = input("Digite o nome do time 1: ")
gols1 = int(input("\nDigite a quantidade de gols marcados pelo time 1: "))

time2= input("\nDigite o nome do time 2: ")
gols2 = int(input("\nDigite a quantidade de gols marcados pelo time 2: "))

if gols1>gols2:
    print(f"O TIME {time1} VENCEU! ")
elif gols1<gols2:
    print(f"O TIME {time2} VENCEU! ")
else:
    print("Empate. ") 