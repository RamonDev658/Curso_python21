primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

if primeiro_valor > segundo_valor:
  print(f'{primeiro_valor=} é maior que {segundo_valor=}')
elif primeiro_valor < segundo_valor:
  print(f'{primeiro_valor=} é menor que {segundo_valor=}')
else: primeiro_valor != segundo_valor
print('Digite um número válido, seu arrombado!')