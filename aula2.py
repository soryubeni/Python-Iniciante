'''
trabalho_terminado = False
if trabalho_terminado == True:
    print('Opa, bora dar uma saída!')
else:
    print('Não posso sair agora...')
'''

'''
print('Você pode me ajudar a carregar essas caixas até o quintal?')
print('Se eu estiver livre sim.')
estou_livre = False
if estou_livre == True:
    print('Ok posso sim')
else:
    print('Peça para alguém te ajudar')
'''

'''
print('Bom dia, cheguei atrsado... posso entrar?')
numero_de_atrasos = 0
if numero_de_atrasos >= 3:
    print('Não, você está suspenso.')
elif numero_de_atrasos == 2:
    print('Pode, mas na próxima falta levará suspensão.')
elif numero_de_atrasos == 1:
    print('Pode entrar, só tome cuidado com as ausências.')
else:
    print('Pode entrar.')
'''

primeiro_valor = input('Digite o primeiro valor:')
segundo_valor = input('Digite o segundo valor:')
if int(primeiro_valor) > int(segundo_valor):
    print('O primeiro valor é maior.')
else:
    print('O segundo valor é maior.')