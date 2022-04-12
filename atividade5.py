from xml.dom.minidom import Notation


notas = []
for nota in range(0, 5):
  nota = int(input(f'Digite a nota {nota}: '))
  notas.append(nota)

print(notas)
notaTotal = 0
for nota in notas:
  notaTotal += nota
  print(notaTotal)
