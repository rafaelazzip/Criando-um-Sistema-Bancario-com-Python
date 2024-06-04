menu = """

Escolha uma das seguintes opções:

[d] Para Depósito
[s] Para Sacar
[e] Para exibir o Extrato
[q] Para Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        #implementar operação de deposito
        valor = float(input("\nInforme o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso! \n")

        else:
            print("\nA operação falhou! O valor informado é inválido.\n")

    elif opcao == "s":
        #implementar operação de saque
        valor = float(input("\nInforme o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nA Operação falhou! Você não possui saldo suficiente para executar essa Operação.\n")

        elif excedeu_limite:
            print("\nA Operação falhou! O valor de saque excede o limite contratado.\n")

        elif excedeu_saques:
            print("\nA Operação falhou! Número máximo de saques excedido.\n")

        elif valor > 0: 
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso! \n")
            numero_saques += 1

        else:
            print("\nA Operação falhou! O valor informado é inválido.\n")


    elif opcao == "e":
        #implementar operação de extrato
        print("\n\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================\n")

    elif opcao == "q":
        break

    else: print("\nOperação inválida, por favor selecine novamente a operação desejada.\n")