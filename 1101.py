"""
Lê um conjunto de números, converte as strings para inteiros e enquanto um dos valores for maior que zero, verifica o menor e o maior valor, para saber de onde até onde devemos calcular e exibir os números.

Então inicializa um vetor com o tamanho da distância entre M e N e vai neste vetor vai colocando em cada posição, os valores inteiros e incrementando até chegar do menor até o maior. No mesmo momento é calculada a soma dos valores entre o menor e maior.

No final, imprimimos o vetor e a soma dos números entre o menor valor e o maior valor
"""

# Lê os valores M e N - Strings
Ms, Ns = input().split()

# Converte M e N para inteiro
M = int(Ms)
N = int(Ns)

# Enquanto M e N forem maior do que zero, então continua fazendo as ações
while (M > 0 and N > 0):

  # Verifica qual é o menor e o maior valor entre M e N
  if M > N:
    menor = N
    maior = M
  else:
    menor = M
    maior = N

  # Começo dos cálculos, inicializando variáveis do vetor e da soma
  i = 0
  vetor = [0]* ((maior - menor) + 1)
  soma = 0

  # Realiza o cálculo de inteiro entre o menor e o maior valor, atribuindo em cada posição os valores e somando-os
  for x in range(menor,maior + 1):
    vetor[i] = x
    i += 1
    soma += x
  # imprime o vetor e o resultado da soma
  for i in range(0,len(vetor)):
    print(vetor[i], end =" ")
  print ('Sum=%d' % soma)

  # Lê novamente os valores de M e N
  Ms, Ns = input().split()
  M = int(Ms)
  N = int(Ns)