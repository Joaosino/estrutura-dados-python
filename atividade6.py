notas = []
notaMaior = 0
notaMenor = 0
notaMedia = 0
for nota in range(0, 4):
  nota = int(input(f'Digite a nota {nota}: '))
  notas.append(nota)
  if nota > notaMaior:
    notaMaior = nota
  if notas.length() == 0:
    notaMenor = nota
  else:
    if nota < notaMenor:
      notaMenor = nota
  notaMedia += nota
notaMedia = notaMedia / 4
print(f'A sua média é {notaMedia}')
print(f'A sua maior nota é {notaMaior}')
print(f'A sua menor nota é {notaMenor}')
print(notas)
