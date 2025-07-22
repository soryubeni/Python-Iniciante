#medidor de velocidade

'''
1. Quais são os dados de entrada necessários? 
velocidade do usuario

2. O que devo fazer com estes dados? 
comparar com a velocidade maxima permitida

3. Quais são as restrições deste problema? 
nenhuma

4. Qual é o resultado esperado? 
exibir mensagens diferentes que corresponde ao nível a multa que o usuario levou

5. Qual é a sequência de passos a serem feitas para chegar ao resultado esperado?
velocidade_maxima_permitida = 80
input velocidade_do_usuario
if velocidade_do_usuario <= 80
    print não houve multa
if velocidade_do_usuario > velocidade_maxima_permitida e velocidade_do_usuario <= velocidade_maxima_permitida +10:
    print levou multa leve
if velocidade_do_usuario > velocidade_maxima_permitida +11 e velocidade_do_usuario <= velocidade_maxima_permitida +20:
    print levou multa grave
if velocidade_do_usuario > velocidade_maxima_permitida +20:
    print levou multa gravissima
'''

velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('Você não levou multa!')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima +10:
    print('Levou multa leve')
elif velocidade >= velocidade_maxima +11 and velocidade <= velocidade_maxima +20:
    print('Levou multa grave')
elif velocidade > velocidade_maxima +20:
    print('Levou multa gravíssima!')