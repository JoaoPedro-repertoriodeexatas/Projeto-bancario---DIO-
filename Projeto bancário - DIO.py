lista_de_operacoes = []
saldo = 0
limite_saque = 500
numero_saques = 0
limite_saques_diarios = 3

print("Olá, este é o seu banco de operações bancárias")
acao = input("Qual ação deseja realizar?")
while True:
    if acao == "d":
        deposito = float(input("Informe o valor a ser depositado:"))
        if deposito > 0:
            saldo += deposito
            lista_de_operacoes.append(deposito)
            print(f'valor depositado: {deposito:.2f}')
        else:
            print("Ação inválida, valor nao cumpre com os requisitos para depósito")

    elif acao == "s":
        if numero_saques <= limite_saques_diarios:
            saque = float(input("Digite o valor que deseja sacar:"))
            if saque <= limite_saque:
                if saque <= saldo:
                    saldo -= saque
                    lista_de_operacoes.append(-saque)
                    print(f"Valor sacado: {saque}")
                    numero_saques += 1
                else:
                    print("Opa, parece que você nao tem saldo suficiente para sacar este valor!")
            else: print("Opa! Parece que esta tentando sacar mais do que o seu limite permite, esta ação nao pode ser realizada")
        else:
            print("Você ja excedeu o seu limite de saques diários, tente novamente outro dia")

    elif acao == "e":
        print("==========EXTRATO==========")
        if lista_de_operacoes == []:
            print("Ainda não foram feitas movimentações")
        else:
            for operacao in lista_de_operacoes:
                if operacao > 0:
                    print(f"Valor depositado: {operacao}")
                elif operacao < 0:
                    print(f"Valor sacado: {-operacao}")
            print(f"O seu saldo atual é: {saldo}")

    elif acao == "q":
        break

    else:
        print("Ação não reconhecida, tente outra vez")
    
    acao = input("Qual ação deseja realizar?")