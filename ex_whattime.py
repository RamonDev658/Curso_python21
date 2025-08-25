# Crie um programa que pergunte a hora e faça a saudação adequada. 

# PRIMEIRA FORMA
while True:
    entrada = input('Que horas são agora?')
    
    try:
        hora = int(entrada)
        
        if 0 <= hora <= 11:
            print('Obrigado, Bom dia!')
            break   # sai do loop
        
        elif 12 <= hora <= 17:
            print('Obrigado, Boa tarde!')
            break   # sai do loop
        
        elif 18 <= hora <= 23:
            print('Obrigado, Boa noite!')
            break   # sai do loop
        
        else:
            print('Hora inválida, digite entre 0 e 23!')
    
    except ValueError:
        print('Por favor digite apenas números inteiros!')

   