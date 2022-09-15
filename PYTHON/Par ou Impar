# PAR OU IMPAR

from random import randint

def linha():
    print('\n', '>-<'*16)

cont = 0
jogar_mais = 'S'
while jogar_mais in ('S', 'SIM'):
    linha()  
    while True:
        jogador = input('\n [ P ] Par ou  [ I ] Impar?  ').strip().upper()
        if jogador in ('I', 'IMPAR'):
            print(' \n Jogador ===> [ IMPAR ] \n\t\t\t [ PAR ] <=== Computador ')
            break
        elif jogador in ('P', 'PAR'):
            print(' \n Jogador ===> [ PAR ] \n\t\t\t [ IMPAR ] <=== Computador ')        
            break
        else:
            print(' \n\t ** JOGADA INVÁLIDA **')

    linha()
    num_jogador = int(input('\n De [ 0 até 10 ]\n Quantos dedos você vai por:  '))
    num_comput = randint(0, 10)
    while True:
        if -1 < num_jogador < 11:    
            soma = num_jogador + num_comput
            print(f' \n Jogador ===> [ {num_jogador} ] \n\t\t\t [ {num_comput} ] <=== Computador ')        
            if soma %2 == 0:
                print(f' \n\t\t   {soma:^4} \n\t\t DEU PAR')
                if jogador in ('P', 'PAR'):
                    print(' \n\t    ** VOCÊ VENCEU **')
                    cont += 1
                    break                    
                else:                
                    print(' \n\t    ** VOCÊ PERDEU **')           
                    while True:
                        jogar_mais = input('\n Vamos mais uma? \n [ S ] Sim / [ N ] Não:  ').strip().upper()
                        if jogar_mais in ('S', 'SIM'):
                            break
                        elif jogar_mais in ('N', 'NÃO', 'NAO'):
                            break
                        else:
                            print('\n >>> Não entendi ')
                    break
            if soma %2 == 1:
                print(f' \n\t\t   {soma:^6} \n\t\t DEU IMPAR')
                if jogador in ('I', 'IMPAR'):
                    print(' \n\t     ** VOCÊ VENCEU **')
                    cont += 1
                    break
                else:                
                    print(' \n\t     ** VOCÊ PERDEU **')           
                    while True:
                        jogar_mais = input('\n Vamos mais uma? \n [ S ] Sim / [ N ] Não:  ').strip().upper()
                        if jogar_mais in ('S', 'SIM'):
                            break
                        elif jogar_mais in ('N', 'NÃO', 'NAO'):
                            break
                        else:
                            print('\n >>> Não entendi ')     
                    break       
        else:
            print(' \n\t ** JOGADA INVÁLIDA **')
            num_jogador = int(input('\n De [ 0 até 10 ]\n Quantos dedos você vai por:  '))
    
linha()   
print(f' \n Você conseguiu {cont} vitórias consecutivas')