letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())
somador = 0

for i in range(n):
    v = input()
    for i in range(len(letras)):
        v = v.replace(letras[i], "")
    v = int(v)
    somador += v

print(v)