n1 = int(input('Digite a n1: '))
n2 = int(input('Digite a n2: '))
n3 = int(input('Digite a n3: '))

def calculaNotas(n1=0, n2=0, n3=0):
  media = (n1 + n2 + n3) / 3
  if media <= 4:
    print('REPROVADO')
  elif media > 4 and media < 6:
    print('RECUPERAÇÃO')
  elif media >= 6:
    print('APROVADO')

calculaNotas(n1,n2,n3)
