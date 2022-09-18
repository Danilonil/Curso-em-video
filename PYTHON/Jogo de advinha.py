# chute um numero de 1 a 10

import random
n_aleatorio = random.randint(1,10)
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
tentativas = 5

print('\n Vou pensar em um número entre 1 e 10, \n e quero que você tente adivinhar qual é.')
while tentativas > 0:         
    print(f'\n Você tem {tentativas} chances')
    chute = input('\n Em que número eu estou pensando?  ')
    if chute in numeros:
        tentativas = tentativas - 1        
        if int(chute) > n_aleatorio:
            print(' Chutou alto', end = '')
        elif int(chute) < n_aleatorio:
            print(' Chutou baixo', end = '') 
        elif int(chute) == n_aleatorio:
            print('\n', '-+-'*16)
            print('\n\t ** Acertou mizerave **')    
            print('\n', '-+-'*16)
            break
        if tentativas == 0:
            print('\n', '-+-'*16)
            print('\n\n\t ** Você perdeu **')
            print('\n', '-+-'*16)
        elif tentativas > 0:
            print(', Tente novamente')
            print('\n', '-+-'*16)
    else:
        print('  ** Numero invalido **')
        print('\n', '-+-'*16)

if int(chute) == n_aleatorio:
    print(f'\n Você usou {5 - tentativas} tentativas para acertar')
else:
    print(f'\n Você usou todas as {5 - tentativas} tentativas')
print(f'\n O número que eu estava pensando era o {n_aleatorio}')
