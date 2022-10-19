mergulhou, retornou = input().split()
identificadores = list(map(int, input().split()))
mergulhou = int(mergulhou)
retornou = int(retornou)
y = 0
faltam = []

while y < mergulhou:
    y = 1
    for i in identificadores:
        if y != i:
            faltam.append(y)
    y += 1

print(faltam)