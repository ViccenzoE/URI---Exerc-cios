# -*- coding: utf-8 -*-

#percorrer o tamanho da string toda em minúsculo
p = str(input().lower())

#contador para somar o total de letras
contador = len(p)

#verifica se o somador tem menos de 10 caracteres ou não e imprime conforme isso
if contador < 10:
    print("palavrinha")
else:
    print("palavrao")