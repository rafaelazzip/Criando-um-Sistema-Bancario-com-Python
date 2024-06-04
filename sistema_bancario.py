menu = """"

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
    elif opcao == "s":
        #implementar operação de saque
    elif opcao == "e":
        #implementar operação de extrato
    elif opcao == "q":
        break

    else: print("Operação inválida, por favor selecine novamente a operação desejada.")