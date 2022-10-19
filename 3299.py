# -*- coding: utf-8 -*-

#variável para informar o número
n = str(input())
contador = ''

#verificador se o número 13 está dentro do valor informado
if '13' in n:
    contador = 's' #atribui 's' à variável caso esteja

#se a variável estiver com 's', então imprimirá que é um número da sorte. Caso contrário, não
if contador == 's':
    print(n + " es de Mala Suerte")
else:
    print(n + " NO es de Mala Suerte")        