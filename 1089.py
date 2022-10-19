# -*- coding: utf-8 -*-
while True:
    n, r = map(int, input().split())
    v = list(map(int,input().split()))
    faltam = []
    resultado = ''

    for i in range(1, n+1):
        if i not in v:
            faltam.append(i)
        
    if faltam == []:
        print("*")
    else:
        "".join([str(faltam) for x in faltam])
        print(resultado + " ")
