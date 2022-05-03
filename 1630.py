# função que permite calcular o MDC
def mdc(a, b):
  while(b != 0):
    resto = a % b
    a = b
    b = resto
  return a

while True:
  try:
    xs,ys = input().split()
    x = int(xs)
    y = int(ys)
    # Em um terreno quadrado precisa só de 4 estacas
    if x == y:
      print(4)
    else:
      # Caso não seja um quadrado, divide as estacas com um intervalo igual ao mdc entre x e y.
      divisorcomum = mdc (x, y)
      print ('%d' % (2 * ( x/ divisorcomum) + 2 * (y / divisorcomum)))
  except EOFError :
    break