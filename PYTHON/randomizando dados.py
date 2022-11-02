
from random import randint

jogadores = []
jogador = {}
pos = 1
desempate = 0
for n in range(4):
    jogador['jogador'] = f'jogador{n+1}'
    jogador['dado'] = randint(1,6)
    jogadores.append(jogador.copy())

#sort para dicionario dentro de lista 
ranking = sorted(jogadores, key = lambda x: x['dado'], reverse = True) 
for item in ranking:
    for k , v in item.items():
        if k == 'jogador' and desempate == item['dado']:
            print(f' {pos-1}°- {v}', end = ' ')
        elif k == 'jogador' and desempate != item['dado']:
            print(f' {pos}°- {v}', end = ' ')
        else:
            print(f'tirou {v}')
            pos +=1
            desempate = v
            print('test')






