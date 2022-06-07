"""
Lê quantos casos de teste serão calculados pelo programa.

Para cada caso de teste, lê os valores de A, B e C e calcula o valor máximo de uma equação de segundo grau considerando que o A sempre é negativo, então a parábola é sempre com a concavidade voltada para baixo. Dessa forma, o ponto máximo é calculado por Yv = - (Delta / 4a)

Considerar Delta = b² - 4ac
"""

# Leitura da quantidade de casos a serem verificados pelo programa
casos = input()
qtdcasos = int(casos)

# Para cada caso, recebe A, B e C, para calcular o valor do ponto máximo
for x in range(0,qtdcasos):
  # Recebe os valores de A, B e C
  As, Bs, Cs = input().split()
  # Converte os valores de A, B e C para inteiro
  A = int(As)
  B = int(Bs)
  C = int(Cs)

  # Calcula ponto maximo Yv
  Yv = -((B * B) - (4 * A * C)) / (4 * A)
  # Imprime o valor do ponto maximo Yv
  print ('%.02f' % Yv)
