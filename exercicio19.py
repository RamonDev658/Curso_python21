# Crie um programa que pergunte a hora e faça a saudação adequada.

entrada = input('Que horas são agora: ')

try:
    hora = int(entrada)
    
    if 0 <= hora <= 11:
        print('Obrigado, Bom dia!')
        
    elif 12 <= hora <= 17:
        print('Obrigado, Boa tarde!')
       
    elif 18 <= hora <=23:
        print('Obrigado, Boa noite!')
       
    else:
        print('Hora inválida, digite entre 0 e 23!')
        
except:
        print('Por favor digite apenas números inteiros!')
    