## WHILE

"""Executa uma ação enquanto uma condição for verdadeira """


condicao = True

while condicao :
    nome = input('Qual o seu nome?')
    print(f'Seu nome é {nome}')
    
    
    if nome == 'sair':
        print('Entendi , até logo!')
        break
    
print('Acabou')   