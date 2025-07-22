'''
1. Quais são os dados de entrada necessários? 
um numero

2. O que devo fazer com estes dados? 
calcular o fatorial do numero passado para o programa e exibir na tela

3. Quais são as restrições deste problema? 
deve ser um numero de valor positivo e inteiro

4. Qual é o resultado esperado? 
é que o fatorial do numero providenciado seja exibido

5. Qual é a sequência de passos a serem feitas para chegar ao resultado esperado? 
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
    fatorial = fatorial * numero
print fatorial
'''
numero = int(input('Digite um numero'))
if numero >0:
    fatorial = 1
    for item in range(1,numero +1):
        fatorial = fatorial * item
    print(fatorial)