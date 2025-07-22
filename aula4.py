'''
# Coleções (listas)
precos = [20,50,200]
#indice:   0, 1, 2
print(precos[0])
print(precos.index(200))

#lista
diversidades = [15, 'Lucas', True]
print(diversidades[1])

#laços em iteráveis
for preco in precos:
    print(preco)
'''

idades = [15,46,74,34,23]
total = 0
for idade in idades:
    total = total + idade
print(total)