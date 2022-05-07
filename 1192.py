# Começo do programa
# Quantidade de casos
casos = int(input())

# Para cada caso, verifica o jogo de Paula
for x in range(0,casos):
  caso = input()
  A = int(caso[0])
  letra = caso[1]
  B = int(caso[2])

  # Se A for igual a B, multiplica
  if (A == B):
    print (A * B)
  # Se a letra for maiuscula, deve subtrair A de B 
  elif (letra.isupper()):
    print (B - A)
  # Senão a letra é minúscula, então deve somar A com B
  else:
    print (A + B)