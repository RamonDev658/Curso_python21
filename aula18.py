#Exercício

"""
Peça ao usuário para digital seu nome
Peça ao usuário para digital sua idade

Se nome e idade forem digitados:
    Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Seu nome contém (ou não) espaços
    Seu nome tem n letras
    A primeira letra do seu nome é {letra}
    A ultima letra do seu nome é {letra}
    
Se nada for digitado em nome ou idade:
Exiba : "Desculpe, você deixou campos vazios."
"""
nome = input("Digite o seu nome: ")

idade = input("Digite a sua idade: ")

if nome  and idade != None :
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:    
        print('Seu nome não contém espaços')
    
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}.')
    print(f'A ultima letra do seu nome é {nome[-1]}.')
else:
     
    print('Desculpe você não preencheu as informações')