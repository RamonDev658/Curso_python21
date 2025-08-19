## Operadores lógicos

"""and (e) or (ou) not (não)

   and - Todas as condições precisam ser verdadeiras

   Se qualquer valor for falso, a expressão inteira será avaliada nesse valor

   São valores falsy: 0 , 0.0, '', False

   Também existe o tipo None que é usado para representar um não valor.

"""


entrada = input('[E]ntrar [S]air: ').strip().upper()
senha_digitada = input('Senha: ').strip()

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
elif entrada == 'S':
    print('Sair')
else:
    print('Opção inválida')


