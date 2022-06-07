# Começo do programa
# Quantidade de numeros
numeros = int(input())

pontuacao = 1
consecutivos = 1
vetor = input().split()

numeroatual = vetor[0]
# Para cada caso, verifica os numeros consecutivos
for i in range(1,numeros):
  
  if(vetor[i] == numeroatual):
    consecutivos += 1
  else:
    consecutivos = 1
    numeroatual = vetor[i]
  if (pontuacao < consecutivos):
    pontuacao = consecutivos
  i += 1
print (pontuacao)