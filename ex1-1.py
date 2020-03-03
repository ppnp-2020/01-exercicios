cambio = 0.23

escolha = int(input('Digite 1 para conversão para USD, 2 para BRL: '))

if escolha == 1:
    valor = int(input('Digite um valor em BRL para conversão: '))
    resultado = valor * cambio 

    print('O valor convertido é USD ' + str(resultado))
elif escolha == 2:
    valor = int(input('Digite um valor em USD para conversão: '))
    resultado = valor * cambio 

    print('O valor convertido é BRL ' + str(resultado))