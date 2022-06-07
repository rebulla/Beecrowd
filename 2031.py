"""
Lê quantos casos de teste serão calculados pelo programa.

Para cada caso de teste, avalia a ação dos jogadores 1 e 2, da seguinte forma:

Ataque Aéreo vs. Pedra: Neste caso, o jogador com o Ataque Aéreo derrota o jogador com a Pedra, por razões óbvias.
Pedra vs. Papel: Neste caso, o jogador com a Pedra derrota o com Papel, porque a Pedra machuca muito mais.
Papel vs. Ataque Aéreo: Aqui o Ataque Aéreo ganha, porque Ataque Aéreo sempre ganha e o Papel é patético.
Papel vs. Papel: Nesta variação, ambos os jogadores ganham, porque o Papel é inútil e ninguém que enfrenta o Papel pode perder.
Pedra vs. Pedra: Para este caso não há ganhador, porque depende do que os jogadores decidem fazer com a Pedra e normalmente não fazem nada.
Ataque Aéreo vs. Ataque Aéreo: Quando isto acontece, todos os jogadores perdem, devido a Aniquilação Mútua.
"""

# Leitura da quantidade de casos a serem verificados pelo programa
casos = input()
qtdcasos = int(casos)

# Para cada caso, recebe a jogada do jogador 1, depois a jogada do jogador 2 e verifica as jogadas de acordo com as regras definidas pelo jogo
for x in range(0,qtdcasos):
  jogador1 = input()
  jogador2 = input()

  # Jogada Ataque Aéreo vs. Pedra: Neste caso, o jogador com o Ataque Aéreo derrota o jogador com a Pedra, por razões óbvias.
  if (jogador1 == 'ataque' and jogador2 == 'pedra'):
    print('Jogador 1 venceu')
  elif (jogador2 == 'ataque' and jogador1 == 'pedra'):
    print('Jogador 2 venceu')

  # Jogada Pedra vs. Papel: Neste caso, o jogador com a Pedra derrota o com Papel, porque a Pedra machuca muito mais.
  if (jogador1 == 'pedra' and jogador2 == 'papel'):
      print('Jogador 1 venceu')
  elif (jogador2 == 'pedra' and jogador1 == 'papel'):
    print('Jogador 2 venceu')

  # jogada Papel vs. Ataque Aéreo: Aqui o Ataque Aéreo ganha, porque Ataque Aéreo sempre ganha e o Papel é patético.
  if (jogador1 == 'papel' and jogador2 == 'ataque'):
    print('Jogador 2 venceu')
  elif (jogador2 == 'papel' and jogador1 == 'ataque'):
    print('Jogador 1 venceu')
  # Jogada Papel vs. Papel: Nesta variação, ambos os jogadores ganham, porque o Papel é inútil e ninguém que enfrenta o Papel pode perder.
  if (jogador1 == 'papel' and jogador2 == 'papel'):
    print('Ambos venceram')

  # jogada Pedra vs. Pedra: Para este caso não há ganhador, porque depende do que os jogadores decidem fazer com a Pedra e normalmente não fazem nada.
  if (jogador1 == 'pedra' and jogador2 == 'pedra'):
    print('Sem ganhador')

  # jogada Ataque Aéreo vs. Ataque Aéreo: Quando isto acontece, todos os jogadores perdem, devido a Aniquilação Mútua.
  if (jogador1 == 'ataque' and jogador2 == 'ataque'):
    print('Aniquilacao mutua')
    

  
