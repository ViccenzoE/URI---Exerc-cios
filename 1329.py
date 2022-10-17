# -*- coding: utf-8 -*-
while 1:
    qtd = int(input())

    if(qtd == 0):
        break

    resultados = list(map(int, input().split()))
    m = 0
    j = 0
        
    for x in resultados:
        if (x == 0):
            m += 1
        else:
            j += 1

    print("Mary won %d times and Jhon won %d times" %(m, j))