# programa para somar números positivos

soma = 0

while True:
    entrada = input("Digite um número positivo (ou 'sair' para encerrar): ")
    
    if entrada.lower() == "sair":
        break
    
    if not entrada.isdigit():
        print("Digite apenas números!")
        continue   # volta pro início do while
    
    numero = int(entrada)
    
    if numero < 0:
        print("Número negativo ignorado!")
        continue   # volta pro início do while
    
    soma += numero
    print(f"Soma atual: {soma}")

print(f"Soma final = {soma}")
