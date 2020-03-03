idade = int(input('Digite sua idade: '))

if idade < 18 or idade >= 65:
    print('Sua idade não permite a realização do empréstimo')
else:
    renda = int(input('Digite sua renda: '))
    valor_emprestimo = int(input('Digite o valor para o empréstimo: '))
    quantidade_parcelas = int(input('Digite a quantidade de parcelas: '))

    montante = valor_emprestimo * (1 + 0.015) ** quantidade_parcelas

    valor_parcela = montante / quantidade_parcelas

    if valor_parcela > renda / 3:
        print('O valor da parcela não pode ser maior que 1/3 da sua renda')
    else:
        print('O empréstimo no valor de ' + str(valor_emprestimo) + ' foi aprovado')
        print('O valor da parcela será ' + str(valor_parcela))
        print('O valor total dos pagamentos é ' + str(montante))
