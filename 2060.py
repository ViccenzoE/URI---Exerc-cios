# -*- coding: utf-8 -*-
n = int(input())
l = input().split()
n2 = 0
n3 = 0
n4 = 0
n5 = 0

for i in range(n):
    if int(l[i]) % 2 == 0:
        n2 += 1
    if int(l[i]) % 3 == 0:
        n3 += 1
    if int(l[i]) % 4 == 0:
        n4 += 1
    if int(l[i]) % 5 == 0:
        n5 += 1

print('%d Multiplo(s) de 2' %n2)
print('%d Multiplo(s) de 3' %n3)
print('%d Multiplo(s) de 4' %n4)
print('%d Multiplo(s) de 5' %n5)