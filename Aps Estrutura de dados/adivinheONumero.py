import random

from menuAps import menuInicial

def guess(x):
  randomico = random.randint(1,x)
  guess = 0
  while guess != randomico:
    guess = int(input(f'escolha um número entre 1 e {x}: '))
    if guess < randomico:
      print("Desculpe, tente novamente. Muito baixo!")
    elif guess > randomico:
      print("Desculpe, tente novamente. Muito alto.")
  print(f"Acerto misevaví! você chutou o número {guess} corretamente!")

def computer_guess(x):
  low = 1
  high = 10
  feedback = ''
  while feedback != 'c':
    guess = random.randint(low, high)
    feedback = input(f"Chutei o número {guess}, foi muito alto?(A), Baixo?(B) ou correto?(C)").lower()
    if feedback == 'h':
      high = guess - 1
guess(10)