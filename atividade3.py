idade = int(input('Digite a sua idade(de 0 a 100 anos): '))
if idade < 0 or idade > 100:
  print('idade inválida!')
elif idade >= 0 and idade < 13:
  print('Criança')
elif idade >= 13 and idade < 18:
  print('Adolescente')
elif idade >= 18 and idade < 100:
  print('Adulto')
