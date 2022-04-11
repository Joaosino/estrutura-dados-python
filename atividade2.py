def calculaGasto():
  KMlitro = 12;
  velocidadeMedia = int(input('Digite a velocidade média da viagem: '));
  tempoGasto = int(input('Digite o tempo de percurso: '))
  distanciaPercorrida = tempoGasto * velocidadeMedia
  litrosUsados = distanciaPercorrida / KMlitro
  print(f'a velocidade média da viagem foi {velocidadeMedia}, o tempo gasto foi {tempoGasto}, a distancia total é de {distanciaPercorrida} e o total de litros gastos foi de {litrosUsados}')

calculaGasto()