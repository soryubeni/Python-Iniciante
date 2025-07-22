'''
Chute o numero

1. Quais são os dados de entrada necessários? 
valor aleatorio de 1 a 10
chute do usuario

2. O que devo fazer com estes dados? 
comparar o chute do usuario com o  valor gerado e dizer se o chute foi maior, menor ou igual ao valor gerado.

3. Quais são as restrições deste problema? 
deve ser apenas um valor de 1 a 10.

4. Qual é o resultado esperado? 
que o programa informe se o chute foi acima, abaixo ou igual ao valor aleatório gerado.

5. Qual é a sequência de passos a serem feitas para chegar ao resultado esperado? 
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio:
    print "Chute muito alto!"
if chute < valor_aleatorio:
    print "Chute muito baixo!"
if chute = valor_aleatorio
    print ""Parabéns, você acertou!
'''

import random
valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10: '))
    if chute > valor_aleatorio:
        print('Chute muito alto!')
    elif chute < valor_aleatorio:
        print('Chute muito baixo!')
    elif chute == valor_aleatorio:
        acertou = True
        print('Parabéns, você acertou!')