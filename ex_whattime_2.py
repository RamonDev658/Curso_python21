# Crie um programa que pergunte a hora e faça a saudação adequada. 



    #SEGUNDA FORMA
    
def obter_hora():
    """Solicita e valida a entrada do usuário."""
    while True:
        entrada = input("Que horas são agora (0-23): ")
        if entrada.isdigit():  # checa se é número positivo
            hora = int(entrada)
            if 0 <= hora <= 23:
                return hora
            else:
                print("Hora inválida! Digite um valor entre 0 e 23.")
        else:
            print("Entrada inválida! Digite apenas números inteiros.")


def saudacao(hora):
    """Retorna a saudação de acordo com a hora."""
    if hora < 12:
        return "Bom dia!"
    elif hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"


# Programa principal
hora_atual = obter_hora()
print(f"Obrigado, {saudacao(hora_atual)}")

