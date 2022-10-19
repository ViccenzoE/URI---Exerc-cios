# -*- coding: utf-8 -*-

#crio variáveis para armazenar o mínimo de alunos
n, k = input().split()
k = int(k)

#transformo o input dos horários em uma lista
a = list(map(int, input().split()))
contador = 0 #contador para ver quantos estão certos

#percorre a minha lista para verificar quais tem horário inferior a zero (horarios certos)
for i in a:
    if i <= 0:
        contador += 1 #soma no contador

#verifica se o contador é menor ou igual ao minimo desejado e imprime se essa turma terá treinamento ou não
if contador >= k:
    print('YES')
else:
    print('NO')