'''
2471 - Codificador de strings
1 - Lê uma string, conta quantas posições de 'a' a 'Z' tem nessa string. Além disso lê um número D, que servirá para deslocar D posições do caractere da string 
2 - Converte a string em ASCII e desloca D posições para cada caractere e conta quantas posições tem.
3 -  Imprime a string e a quantidade obtida no passo 1
4 - Imprime a string obtida no passo 2 e a quantidade obtida no passo 2
5 - Se a quantidade de 1 for igual a quantidade de 2, então imprime 'Codificação Perfeita!', caso contrário imprime 'Codificação Não Perfeita!'

'''
# Lê o vetor 's'
s = input() 

# Lê D, que servirá para deslocar as posições do ASCII do vetor 's'
Ds = input()
D = int(Ds)

# Para contar o tamanho de 's' com posições válidas
tamanhoS = 0
for i in range(len(s)):
  # Verifica se o vetor tem está entre 'a' a 'z' ou 'A' a 'Z'
  if (ord(s[i]) in (range(32,127)) ):
    tamanhoS += 1
# Imprime 's' e o tamanho de posições válidas
print (s, tamanhoS)


# Codifica o vetor 's'
sCodificada = ""
for i in range(len(s)):
  sCodificada += str(chr(ord(s[i]) + D))

# conta o tamanho de posições válidas da codificada
tamanhosCodificada = 0

for i in range(len(sCodificada)):
  # Verifica se o vetor tem está entre 'a' a 'z' ou 'A' a 'Z'
  if (ord(sCodificada[i]) in (range(32,127)) ):
    tamanhosCodificada += 1

# Imprime 's' codificado e o tamanho de posições válidas
print(sCodificada, tamanhosCodificada)

# Verifica se as posições válidas são iguais
if (tamanhoS == tamanhosCodificada):
  print("Codificação Perfeita!")
else:
  print("Codificação Não Perfeita!")

