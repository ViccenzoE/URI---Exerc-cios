# -*- coding: utf-8 -*-
while True:
   n = int(input())
   if n == 0: break
   s = 0
   for i in range(n):
        c,v =  input().split()
        c = int(c)
        v = int(v)
        s += v//2

   print(s//2)