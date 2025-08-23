## CONSTANTES
"""Variáveis que não vão mudar, escreva em uppercase.
"""


entrada = input('Digite um número inteiro: ') 

if entrada.isdigit():  # checando se foi digitado um número
    entrada_int = int(entrada) # convertendo em int
    par_impar = entrada_int % 2 == 0 # checando se o numero é par
    par_impar_text = 'impar'

    if par_impar:
        par_impar_text = 'par'
        
    print(f'O número {entrada_int} é {par_impar_text}')
else:
    print(f'Você não digitou um número inteiro!')        