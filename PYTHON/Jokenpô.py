# JOKENPO

def linha():
    print('\n', '<->'*16)

import random
import time

jogada = ['[0]\tPEDRA', '[1]\tPAPEL', '[2]\tTESOURA']
repete = True
while repete == True:
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
        if jogador == 2 or comput == 2:
            if jogador == 2 and comput == 0:
                print('\n\t\t** Você perdeu **'.upper())
            elif jogador == 2 and comput == 1:
                print('\n\t\t** Você venceu **'.upper())
            elif jogador == 2 and comput == 2:
                print('\n\t\t** Empatou **'.upper())
            elif comput == 2 and jogador == 0:
                print('\n\t\t** Você venceu **'.upper())
            elif comput == 2 and jogador == 1:
                print('\n\t\t** Você perdeu **'.upper())
        elif jogador > comput:
            print('\n\t\t** Você venceu **'.upper())
        elif jogador == comput:
            print('\n\t\t** Empatou **'.upper())
        elif jogador < comput:
            print('\n\t\t** Você perdeu **'.upper())
        linha()
        
        resposta = ''
        while resposta != 'N' and resposta != 'S':
            print('\n >>>>> Vamos de novo? \n\t <[S] Para jogar novamente> \n\t <[N] Para desistir>')
            resposta = input('\n').upper().strip()
            if resposta in ('S', 'SIM'):
                repete = True
            elif resposta in ('NÃO', 'NAO', 'N'):
                repete = False                               
            elif resposta != 'N' and resposta != 'S':         
                print('\n Não entendi', end = '')
            
    else:
        print('\t ** Jogada inválida **\n')
        linha()
        repete = True
    
print('\n Obrigado por jogar ')