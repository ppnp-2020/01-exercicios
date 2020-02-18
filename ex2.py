conta_cadastrada = '1234'
senha_cadastrada = '101112'
saldo = 100

conta_informada = input('Digite o número da conta: ')

if conta_informada == conta_cadastrada:
  senha_informada = input('Digite a senha: ')

  if senha_informada == senha_cadastrada:
    valor_saque = int(input('Digite o valor para saque: '))

    if saldo >= valor_saque:
      saldo = saldo - valor_saque
      print('Saque efetuado com sucesso')
      print('O saldo atualizado é ' + str(saldo))

    else:
      print('Saldo insuficiente')
  else:
    print('Senha inválida')
else:
  print('Conta inválida')
