# -*- coding: utf-8 -*-

#fazer uma lista com os valores tanto de apostado quanto de sorteado como inteiros
num = list(map(int, input().split()))
sort = list(map(int, input().split()))
contador = 0

#percorrer os números que foram apostados e verificar se estão dentro da lista de sorteados. Caso não estejam, adiciona 1 ao contador
for i in num:
    if i in sort:
        contador += 1

#de acordo com o valor do contador, verifica qual será a saída
if contador == 3:
    print("terno")
elif contador == 4:
    print("quadra")
elif contador == 5:
    print("quina")
elif contador == 6:
    print("sena")
else:
    print("azar")