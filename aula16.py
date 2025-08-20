## Formatação básica de strings com f-strigs
"""
f-float,
.<número de dígitos>f,
(caracteres)(><^)(quantidade),
>-Esquerda,
<-Direita,
^-Centro,
Sinal- + ou -,
Ex.: 0>-100,.1f
Conversion flag- !r, !s !a
"""
variavel = 'ABCD'
numero = 10333034.434434
print(f'{variavel}')
print(f'{variavel:*>10}')
print(f'{variavel:*<10}')
print(f'{variavel:*^10}')
print(f'{numero:,.2f}')
print(f'O Hexadecimal de {int(numero)} é {int(numero):08X}')
