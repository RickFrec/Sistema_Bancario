menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """

saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
saques_maximos = 3

while True:

    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Valor de R$ {valor} depositado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido!")
        
        

    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_por_saque
        excedeu_saques = numero_saques >= saques_maximos

        if excedeu_saldo:
            print("Você não possui saldo suficiente para esse saque!")

        elif excedeu_limite:
            print("Você excedeu o valor limite para saques!")

        elif excedeu_saques:
            print("Você excedeu o número máximo de saques do dia! tente novamente amanhã!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque no valor de R$ {valor} realizado com sucesso!")

        else:
            print("Operação falhou! O valor de saque tem que ser maior do que 0!")


    elif opcao == "2":
        print("\n=============EXTRATO===============")
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "3":
        break

    else:
        print("A opção selecionada não é valida. Para continuar escolha uma das opções do menu!")
