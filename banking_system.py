
def menu() :
    menu_str = '''\n
==========MENU==========    
[D]\tDepositar
[S]\t Sacar
[E]\t Extrato
[N]\t Nova conta
[L]\t Listar contas
[U]\t Novo usuário
[Q]\t Sair

'''
    return input (menu_str)

def depositar (saldo, valor, extrato, /):
   if valor > 0:
      saldo += valor
      extrato += f'Depósito:\tR$ {valor:.2f}\n'
      print('\n=== Depósito realizado com sucesso!===')
   else:
      print('\n@@@ Operação falhou! Valor informado inválido. @@@')
   return saldo, extrato
   

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
       print('\n@@@ Operação falhou! Você não tem saldo suficient. @@@')
    elif excedeu_limite:
       print('\n@@@ Operação falhou! O valor do saque exede o limite. @@@')
    elif excedeu_saques:
       print('\n@@@ Operação falhou! Número máximo de saques excedido. @@@')
    elif valor > 0:
       saldo -= valor
       extrato += f'Saque: \t\tR$ {valor:.2f}\n'
       numero_saques += 1
       print ('\n === Saque realizado com sucesso!===')
    else:
       print('\n@@@ Operação falhou! O valor informado é inválido.@@@')

    return saldo, extrato, numero_saques

def exibir_extrato(saldo,/, *, extrato):
    print('\n==========EXTRATO==========')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('===========================')

def filtrar_usuario(cpf,usuarios):
   cpf_somente_numeros = ''.join(filter(str.isdigit, cpf))
   usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf_somente_numeros]
   return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
   
    cpf_somente_numeros = "".join(filter(str.isdigit, cpf)) 
    
    usuario = filtrar_usuario(cpf_somente_numeros, usuarios)
  
    if usuario:
      print('\n@@@ Já existe usuário com esse CPF! @@@')
      return
   
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa):')
    endereco = input('Informe o endereço (logradouro, número, bairro, cidade/estado):')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf_somente_numeros, 'endereco': endereco})
    print('=== usuário criado com sucesso!===')

def cadastrar_conta_bancaria(contas, usuarios, numero_conta):
   cpf = input('Informe o CPF:')

   cpf_somente_numeros = ''.join(filter(str.isdigit, cpf))

   usuario = filtrar_usuario(cpf_somente_numeros, usuarios) 

   if not usuario:
      print('\n @@@ Usuário não encontrado, operação encerrada! @@@')
      return None 

   print('\n=== Conta criada com sucesso! ===')

   contas.append({'agencia': '0001', 'numero_conta': numero_conta, 'usuario': usuario}) 
   return {'agencia': '0001', 'numero_conta': numero_conta, 'usuario': usuario}

def listar_contas(contas):
   if not contas:
      print('\n@@@ Nenhuma conta cadastrada. @@@')
      return
   
   for conta in contas:

      linha = f'''\
          Agência:\t{conta['agencia']}
          C/C\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
          
      '''  
      print('='*100)
      print(linha)


saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3 

usuarios = []
contas = []
numero_conta = 1

while True:
    opcao = menu().upper()

    if opcao == 'D':
       valor = float(input('Informe o valor do depósito: '))
       saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == 'S':
         valor = float(input('Informe o valor do saque: '))
         saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
         )

    elif opcao == 'E':
     exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'U':
       cadastrar_usuario(usuarios)

    elif opcao  == 'N':
       conta = cadastrar_conta_bancaria(contas, usuarios, numero_conta)
       if conta:
          numero_conta += 1

    elif opcao == 'L':
          listar_contas(contas)

    elif opcao == 'Q':
       break
    else:
       print('Opção inválida,por favor selecione uma opção válida.')
       



            
    




