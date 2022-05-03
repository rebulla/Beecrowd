# coding: utf-8
"""
    Calcula o mínimo de n números inteiros.
"""


n = int(input())

vet_int = [int(x) for x in input().split()]  


min_int = vet_int[0] # Inicializa o mínimo com o
                     # primeiro número inteiro lido.
pos_min_int = 0 # Inicializa a posição do mínimo com zero
for i in range(1, n): # Compara o segundo número em diante
    if (vet_int[i] < min_int): # Se for menor que o mínimo
        min_int = vet_int[i]   # passa a ser o novo mínimo
        pos_min_int = i # Posição Mínima passa a ser i
print('Menor valor:', min_int) # Escreve o mínimo
print ('Posicao:', pos_min_int) # Escreve posição do mínimo