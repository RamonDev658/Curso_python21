### Try/Except
"""Try- tentar executar o código
    except- ocorreu algum erro ao tentar executar o código
"""

numero = input('Digite um número que vou te dar o dobro: ')

try:
    numero_float = float(numero)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2}')
except:
    print('Isso não é um número seu Zé buceta.')