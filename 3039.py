# -*- coding: utf-8 -*-
n = int(input())
c = ''
contadorF = 0
contadorM = 0

#percorrer o tamanho de crianças que não responderam o que queriam e verificar se o último digito é um F ou um M. Dependendo do que for, soma a quantidade no contador respectivo de carrinhos ou de bonecas
for i in range(n):
    c = str(input())
    if c[-1] == 'F':
        contadorF += 1
    if c[-1] == 'M':
        contadorM += 1

print("%d carrinhos" %contadorM)
print("%d bonecas" %contadorF)

