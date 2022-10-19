# -*- coding: utf-8 -*-

#entrada do total de peças
n = int(input())

#transformar as peças que ele tem em uma lista e converter os valores para int
p = list(map(int, input().split()))

#percorrer o tamanho do total de peças e verificar se há alguma que não está presente. Se não estiver, ele printa e começa a percorrer novamente com o valor acrescido de um
for i in range(1, n+1):
    if i != 0:
        if i not in p:
            print(i)
