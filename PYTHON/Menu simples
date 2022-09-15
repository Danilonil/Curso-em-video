# MENU

resposta = ''
def linha():
    print('\n', '-+-'*16, '\n')
        
      
n1 = int(input('\n Digita um número aí Zé: '))
n2 = int(input(' Mais um: ')) 
while resposta != '5':
    print('\n O que você quer fazer com esses números? '
              '\n\t [1] Somar \n\t [2] Maior \n\t [3] Multiplicar \n\t [4] Novos números \n\t [5] Sair da simulação')
    resposta = input('\n ')
    linha()
        
    if resposta == '1':
        print(f' {n1} + {n2} = {n1+n2}')
    elif resposta == '2':
        if n1 > n2:
            print(f' {n1} é maior que {n2}')
        elif n1 < n2:
            print(f' {n2} é maior que {n1} ')
        else:
            print(f' Os números {n1} e {n2} são iguais ')         
    elif resposta == '3':
        print(f' {n1} x {n2} = {n1*n2} ')               
    elif resposta == '4':
        print('\n Ok...', end = '')
        n1 = int(input('\n Digita um número aí Zé: '))
        n2 = int(input(' Mais um: ')) 
    elif resposta == '5':
        break
    else:
        print('\t ** inválido **')
    linha()
    
print('\n Obrigado por usar a skynet versão beta')