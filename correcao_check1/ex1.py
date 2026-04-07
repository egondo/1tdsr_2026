consumo_ant = float(input("Consumo do mês anterior: "))
consumo_vig = float(input("Consumo do mês vigente: "))

if consumo_vig < 0:
    print("Valor de consumo inválido!")
    quit()
elif consumo_vig <= 20:
    valor_metro = 2
elif consumo_vig <= 35:
    valor_metro = 3.5
elif consumo_vig <= 50:
    valor_metro = 5.5
else:
    valor_metro = 7

valor_conta = consumo_vig * valor_metro

if consumo_ant > consumo_vig:
    desconto = valor_conta * 0.15
    valor_conta = valor_conta - desconto
    print(f"Sua conta teve um desconto de R$ {desconto:.2f}")
elif consumo_ant < consumo_vig:
    multa = valor_conta * 0.10
    valor_conta = valor_conta + multa
    print(f"Sua conta teve uma multa de R$ {multa:.2f}")

print(f"O valor da conta foi de R$ {valor_conta:.2f}")