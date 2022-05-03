## Código ainda em andamento
consumo = int(input())

agua = 0.00
esgoto = 0.00
if (consumo > 10):
  print ('ok')
  consumo = consumo - 10
  agua = 60.8
  esgoto = 42.6
  print ('Consumo 10: %.02f %.02f' % (agua, esgoto))
  if (consumo > 5):
    consumo = consumo - 5
    agua += 77.9
    esgoto += 54.5
    print ('Consumo 20: %.02f %.02f' % (agua, esgoto))
    if (consumo > 5):
      consumo = consumo - 5
      agua += 79.3
      esgoto += 55.5
      print ('Consumo 30: %.02f %.02f' % (agua, esgoto))
      if (consumo > 5):
        consumo = consumo - 5
        agua += 87.5
        esgoto += 61.3
        if (consumo > 5):
          consumo = consumo - 5
          agua += 107.6
          esgoto += 75.3
          if (consumo > 20):
            consumo = consumo - 20
            agua += 129.0
            esgoto += 90.3
            if (consumo > 0):
              agua += consumo * 14.21
              esgoto += consumo * 9.95
          else: 
            agua += consumo * 12.9
            esgoto += consumo * 9.03
        else: 
          agua += consumo * 10.76
          esgoto += consumo * 7.53
      else:
        agua += consumo * 8.75
        esgoto += consumo * 6.13
    else: 
      agua += consumo * 7.93
      esgoto += consumo * 5.55
  else:
    agua += consumo * 7.79
    esgoto += consumo * 5.45
else:
  agua = consumo * 6.08
  esgoto = consumo * 4.26

print ('Consumo: %d metros cúbicos' % )
print ('Total a pagar: R$ 15.05 + R$ %.02f + R$ %.02f = R$ %.02f' % (agua, esgoto, (agua + esgoto + 15.05)))