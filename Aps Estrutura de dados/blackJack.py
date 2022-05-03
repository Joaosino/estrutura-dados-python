import random
import sys

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4
naipe = ['♥','♦','♣','♠']

def carta_real(v,n): # v de valor e n de naipe.
    print(" _____________________")
    print("|                     |")
    print(f"|  {v}                  |")
    print(f"|  {n}                  |")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print(f"|         {n}           |")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print(f"|                  {n}  |")
    print(f"|                  {v}  |")
    print("|_____________________|")

def jogo():
  print("Bem vindo ao jogo de BlackJack.")
  escolha = int(input("\nDigite 1 para começar ou 0 para voltar: "))
  if escolha == 1:
    jogada(valores)
  else:
    import menuAps
    menuAps.menuInicial()

def jogada(valores):
  mão = []
  for i in range(52):
    val = random.choice(valores)
    print(val)
    if val == 11:
      val = 'J'
    elif val == 12:
      val = 'Q'
    elif val == 13:
      val = 'K'
    elif val == 1:
      val = 'A'
    for n in naipe:
      random.shuffle(naipe)
    carta = str(val) + n
    if carta not in mão:
      mão.append(carta)
    if carta in mão:
      random.shuffle(naipe)
      print(carta)
      valores.remove(val)
  print(mão)
  print(valores)
  print(len(mão))

def carta_extra():
  mao = []
  cartas_extras = 0
  while cartas_extras < 2:
    print("Você gostaria de uma carta extra?")
    escolha = int(input("Digite 1 para sim ou 2 para não: "))
    if escolha == 1:
      cartas_extras += 1
      val = valores.pop()
      if val == 11:
        val = 'J'
      elif val == 12:
        val = 'Q'
      elif val == 13:
        val = 'K'
      elif val == 1:
        val = 'A'
      mao.append(val)
      print(mao)
    else:
      resultado()

def resultado():
  resultado = 0
  for resultado in mao:
    if val == 'J':
      resultado += 11
    elif val == 'Q':
      resultado += 12
    elif val == 'K':
      resultado += 13
    elif val == 'A':
      resultado += 1
    else:
      resultado += val
    print(f"A soma das cartas da sua mão é {resultado}")


jogo()

# while True:
#    carta_extra = int(input("Você gostaria de comprar uma carta extra? \nDigite 1 para sim\nDigite 2 para não\n"))
 #   if carta_extra == 1:
  #      break



# print(f"\nA sua primeira carta é um {X} de {naipe_1}")