'''

'''

rajesh_vence = ['tesoura papel', 'papel pedra', 'pedra lagarto', 'lagarto spock', 'tesoura lagarto', 'lagarto papel', 'papel spock', 'spock pedra', 'pedra tesoura']

def pptls (jogada_rajesh, jogada_sheldon):
  if (jogada_rajesh == jogada_sheldon):
    return 'empate'
  elif ((jogada_rajesh + ' ' + jogada_sheldon) in rajesh_vence):
    return 'rajesh'
  else:
    return 'sheldon'
  
  

# Leitura da quantidade de casos a serem verificados pelo programa
casos = input()
qtdcasos = int(casos)

# Para cada caso, recebe a jogada do jogador 1, depois a jogada do jogador 2 e verifica as jogadas de acordo com as regras definidas pelo jogo
for x in range(0,qtdcasos):
  rajesh, sheldon = input().split()
  print (pptls(rajesh, sheldon))