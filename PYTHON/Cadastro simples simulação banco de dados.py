# CADASTRO DE PESSOAS

def linha():
    print('\n', '=+='*16)

cont_maioridade = cont_h = cont_m = idade_h_velho = 0
mais_users = 'S'
homem_velho = ''

while mais_users in ('S', 'SIM'):
    linha()
    nome = str(input(' \n Qual é o seu nome?:  ')).strip().title()
    idade = int(input(' E sua idade?:  '))
    if idade < 0 or idade > 130: 
        print('\n\t ** IDADE INVÁLIDA **')       
        idade = int(input(' E sua idade?:  '))        
    if idade > 17:
        cont_maioridade += 1
    sexo = str(input(' Sexo? [ M ]/ [ F ]:  ')).strip().upper()
    if sexo not in ('M', 'MASCULINO', 'F', 'FEMININO'):
        print('\n\t ** SEXO INVÁLIDO **')       
        sexo = str(input(' Sexo? [ M ]/ [ F ]:  ')).strip().upper()
    if sexo in ('M', 'MASCULINO'):
        cont_h += 1
        if idade_h_velho < idade:
            idade_h_velho = idade
            homem_velho = nome
    if sexo in ('F', 'FEMININO') and idade < 20:
        cont_m += 1

    while True:
        mais_users = str(input('\n Quer cadastrar um novo usuário? [ S ]/ [ N ]:  ')).strip().upper()
        if mais_users in ('S', 'SIM'):
            break
        elif mais_users in ('N', 'NÃO', 'NAO'):
            break
        else:
            print('\n >>> Não entendi ')

linha()
if cont_maioridade > 0:
    print(f'\n Nesso grupo de pessoas, \n {cont_maioridade} pessoa(s) é(são) maior(es) de idade')
if cont_h > 0:
    print(f' {cont_h} homen(s) foi(foram) cadastrado(s)'
        f'\n E o homem mais velho se chama {homem_velho}')
if cont_m > 0:
    print(f' {cont_m} mulher(es) tem menos de 20 anos')
    