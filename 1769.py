cpf = str(input())
b = ".-"
for i in range(0, len(b)):
  cpf = cpf.replace(b[i], "")

totalB1 = 0
totalB2 = 0
for x in range(len(cpf)):
    if x <= 9:
        totalB1 += int(b[x]) * (int(x) + 1)

print(totalB1)