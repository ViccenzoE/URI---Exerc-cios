# -*- coding: utf-8 -*-
qtd = (int(input())) #entrada da quantidade de elfos
#variáveis para armazenar as horas de cada tipo de trabalho
cB = 0
cA = 0
cM = 0
cD = 0

#percorrer o tamnho da quantidade de elfos
for i in range(qtd):
    #adicionar um elfo e transformar a sua carga horária [2] em inteiro
    elfo = input().split()
    elfo[2] = int(elfo[2])

    #verificar em qual quadrante de trabalho ele se encaixa de acordo com o seu [1], somando no total da variável do trabalho que ele cair
    if elfo[1] == 'bonecos':
        cB += elfo[2]
    elif elfo[1] == 'arquitetos':
        cA += elfo[2]
    elif elfo[1] == 'musicos':
        cM += elfo[2]
    elif elfo[1] == 'desenhistas':
        cD += elfo[2]

#somar todas as divisões inteiras do total de horas de cada um dos tipos de trabalho
total = (cB//8) + (cA//4) + (cD//12) + (cM//6)
print(total)

