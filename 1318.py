bilhetesOriginais, pessoasPresentes = input().split()
totalBilhetes = input().split()
bilhetesOriginais = int(bilhetesOriginais)
pessoasPresentes = int(pessoasPresentes)

for i in range(len(totalBilhetes)):
    totalBilhetes[i] = int(totalBilhetes[i])

numero = 0
contador = 0
repetidos = 0
x = 0


while x <= 10000:
    for y in range(len(totalBilhetes)):
        if x == totalBilhetes[y]:
            contador += 1
            if contador > 2:
                repetidos += 1
                contador = 0
    x += 1

print(repetidos)