"""
Devo ler 3 inteiros, que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.
Para calcular o valor do  Interferência de Comunicação Mágica (ICM), preciso  dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos. 
Ao final do cálculo, basta imprimí-lo
"""

# Lendo os valores de a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.
Ns, Xs, Ys = input().split()

# Convertendo os valores para inteiro
N = int(Ns)
X = int(Xs)
Y = int(Ys)

# Calculando o valor do ICM
ICM = float(N / (X + Y))

# Imprime o valor do ICM
print('%.02f' % ICM)