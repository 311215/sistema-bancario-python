menu = '''

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

'''
saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3 

while True:
    opcao = input (menu)

    if opcao == 'D':
       valor = float(input('Informe o valor do depósito: '))

       if valor > 0:
          saldo += valor
          extrato += f'Depósito: R$ {valor:.2f}\n'
          print('Depósito realizado com sucesso!')
       else:
        print('Falha na operação! O valor informado é inválido')

    elif opcao == 'S':
         valor = float(input('Informe o valor do saque: '))

         excedeu_saldo = valor > saldo
         excedeu_limite = valor > limite
         excedeu_saques = numero_saque >= LIMITE_SAQUE

         if excedeu_saldo:
            print('Você nâo tem saldo suficiente!!')
         elif excedeu_limite:
            print('O valor do saque excede o limite!!')
         elif excedeu_saques:
            print('O valor do saque excede o limite permitido!')
         elif valor >0:
            saldo -= valor
            extrato+= f'Saque: R$ {valor:.2f}\n'
            numero_saque += 1
            print('Saque realizado com sucesso!')

         else:
            print('Operação falhou!! Valor informado é inválido.')

    elif opcao == 'E':
       print('\n=====EXTRATO=====')

       print('Não foram realizadas movimentações.' if not extrato else extrato)
       print(f'\nSaldo: R$ {saldo:.2f}')
       print('=================')
    elif opcao == 'Q':
       break
    else:
       print('opção inválida,por favor selecione uma opção válida.')
       



            
    




