## Fatiamento de strings
"""
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs-> a função len retorna a qtd 
de caracteres da string
"""
variavel = 'Olá mundo'
variavel_2 = 'Rkgaofmfdoren'
print(variavel[0:])# do inicio ao fim, omito a 2a info
print(variavel[0:9])#do início ao fim sem omitir
print(variavel[0:3]) # do início até a parte onde quero parar +1
print(variavel[4:]) # do meio até o final com omissão
print(variavel[::-1]) # do final para o início
print(len(variavel)) #conta caracteres de 1 a 9
print(variavel[0:len(variavel):1]) # pega do inicio até o fim com passo 1 a 1
print(variavel_2[0:len(variavel_2):3]) # pega do inicio até o fim com passo 3 a 3
