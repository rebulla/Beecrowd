# função que permite calcular o MDC
def mdc(a, b):
  while(b != 0):
    resto = a % b
    a = b
    b = resto
  
  return a

N = int(input())

for x in range(N):
    A, B = input().split(' ')
    A, B = int(A), int(B)
    print(mdc(A, B))