# -*- coding: utf-8 -*-

while True:
    try:
        n, r = map(int, input().split())
        v = list(map(int, input().split()))

        t = []
        f = ''
        for i in range(1, n+1):
            t.append(i)
        
        for x in t:
            if x not in v:
                f += str(x) + " "

        if f != '':
            print(f)
        else:
            print('*')
            
    except EOFError:
        break