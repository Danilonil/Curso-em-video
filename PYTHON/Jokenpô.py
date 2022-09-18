def linha():
    print('\n', '<->'*16)

import random
import time

jogada = ['[0]\tPEDRA', '[1]\tPAPEL', '[2]\tTESOURA']
resposta = 'S'
while resposta in 'S':
    comput = random.randint(0,2)      
    linha()
    print('\n >>>> Escolha: ')
    for opcao in jogada:
        print(opcao)
    jogador = input('\n')
    if jogador in ('0', '1', '2'):
        jogador = int(jogador)
        time.sleep(0.5)
        print('\t\t jooookennn...'.upper())
        time.sleep(1)
        print('\t\t\t ...nnpô'.upper())
        time.sleep(0.3)
        print(f' Jogador ====> {jogada[jogador][3:]} \n') # lista[variável][manipulação da string]
        print(f'\n\t\t {jogada[comput][3:]}  <==== Computador') # lista(variavel)
        linha()
        
        time.sleep(1)
        if jogador == 2 and comput == 0:
            print('\n\t\t** Você perdeu **'.upper())
        elif comput == 2 and jogador == 0:
            print('\n\t\t** Você venceu **'.upper())
        elif jogador > comput:
            print('\n\t\t** Você venceu **'.upper())
        elif jogador == comput:
            print('\n\t\t** Empatou **'.upper())
        elif jogador < comput:
            print('\n\t\t** Você perdeu **'.upper())
        linha()
    
        while True:
            print('\n >>>>> Vamos de novo? \n\t <[S] Para jogar novamente> \n\t <[N] Para desistir>')
            resposta = input('\n').upper().strip()
            if resposta in ('s', 'S'):
                break
            elif resposta in ('n', 'N'):
                break                              
            elif resposta != 'N' and resposta != 'S':         
                print('\n Não entendi', end = '')
            
    else:
        print('\t ** Jogada inválida **\n')
        linha()
        repete = True
    
print('\n Obrigado por jogar ')