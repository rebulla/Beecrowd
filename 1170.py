# Começo do programa
# Quantidade de casos
casos = int(input())

# Para cada caso, verifica a quantidade de dias de comida
for x in range(0,casos):
  dias = 0
  kilos = float(input())
  parar = 0

  while parar == 0:
    kilos= kilos/2
    dias+=1

    if kilos <=1:
      parar = 1

      
  print(dias,"dias")