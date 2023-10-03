menu = """
 [1] Depositar
 [2] Sacar
 [3] Extrato 
 [4] Sair
 => """

saldo = 0
limite = 500
extrato = ''
n_saques = 0
l_saques = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input('Digite um valor:'))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('Digite um valor válido.')

    elif opcao == 2:
        valor = float(input('Digite um valor:'))
        execedeu_saldo = valor > saldo
        execedeu_limite = valor > limite
        execedeu_numero = n_saques >= l_saques

        if execedeu_saldo:
            print(f'Você não tem saldo suficiente para esta operação. Seu saldo é de R$ {saldo:.2f}')

        elif execedeu_limite:
            print('Este valor excede seu limite de saque.')

        elif execedeu_numero:
            print('Você excedeu seu limite de saques diários. Você poderá realizar novos saques no prazo de 24h.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            n_saques += 1

        else:
            print('Operação falhou! Digite um número válido.')

    elif opcao == 3:
        print('\n**********| Extrato |**********')
        print(extrato if extrato else 'Não foram realizadas movimentações')
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('==================================')

    elif opcao == 4:
        break

    else:
        print('Operação inválida')

















