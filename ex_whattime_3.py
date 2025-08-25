# Crie um programa que pergunte a hora e faça a saudação adequada. 


# TERCEIRA FORMA 

while True:
    entrada = input("Que horas são agora (0-23): ")
    
    if entrada.isdigit():
        hora = int(entrada)
        if 0 <= hora <= 23:
            print(
                "Obrigado, " +
                ("Bom dia!" if hora < 12 else "Boa tarde!" if hora < 18 else "Boa noite!")
            )
            break
        else:
            print("Hora inválida! Digite entre 0 e 23.")
    else:
        print("Entrada inválida! Digite apenas números inteiros.")
