
import random

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4

def main():
  print("Bem vindo ao jogo de BlackJack.")
  escolhaBlackJack = int(input("\nDigite 1 para começar ou 0 para voltar: "))
  if escolhaBlackJack == 1:
    jogada(valores)
  if escolhaBlackJack == 0:
    menuAps.escolheJogo()

def jogada(valores):
  mão = []
  for i in range(3):
    random.shuffle(valores)
    carta = valores.pop()
    if carta == 11:
      carta = 'J'
    elif carta == 12:
      carta = 'Q'
    elif carta == 13:
      carta = 'K'
    elif carta == 1:
      carta = 'A'
    mão.append(carta)
  print(mão)

def carta_extra():
  cartas_extras = 0
  while cartas_extras < 2:
    print("Você gostaria de uma carta extra?")
    escolha = int(input("Digite 1 para sim ou 2 para não: "))
    if escolha == 1:
      cartas_extras += 1
      carta = valores.pop()
      if carta == 11:
        carta = 'J'
      elif carta == 12:
        carta = 'Q'
      elif carta == 13:
        carta = 'K'
      elif carta == 1:
        carta = 'A'
      mão.append(carta)
      print(mão)
    else:
      resultado()

def resultado():
  resultado = 0
  for resultado in mão:
    if carta == J:
      resultado += '11'
    elif carta == Q:
      resultado += '12'
    elif carta == K:
      resultado += '13'
    elif carta == A:
      resultado += '1'
    else:
      resultado += carta
    print(f"A soma das cartas da sua mão é {resultado}")


if __name__ == "__main__":
  main()