def mudaCor(texto, cor):
  if cor == 'vermelho':
    vermelho = '\033[31m'+texto+'\033[0;0m'
    texto = vermelho
    return texto
  if cor == 'verde':
    verde = '\033[32m'+texto+'\033[0;0m'
    texto = verde
    return texto
  if cor == 'azul':
    azul = '\033[34m'+texto+'\033[0;0m'
    texto = azul
    return texto
  if cor == 'ciano':
    ciano = '\033[36m'+texto+'\033[0;0m'
    texto = ciano
    return texto
  if cor == 'magenta':
    magenta = '\033[35m'+texto+'\033[0;0m'
    texto = magenta
    return texto
  if cor == 'amarelo':
    amarelo = '\033[33m'+texto+'\033[0;0m'
    texto = amarelo
    return texto
  if cor == 'preto':
    preto = '\033[30m'+texto+'\033[0;0m'
    texto = preto
    return texto
  if cor == 'branco':
    branco = '\033[37m'+texto+'\033[0;0m'
    texto = branco
    return texto
  if cor == 'original':
    restaura_cor_original = '\033[0;0m'
    texto = restaura_cor_original
    return texto
  if cor == 'negrito':
    negrito = '\033[1m'+texto+'\033[0;0m'
    texto = negrito
    return texto
  if cor == 'reverso':
    reverso = '\033[2m'+texto+'\033[0;0m'
    texto = reverso
    return texto
  if cor == 'fpreto':
    fundo_preto = '\033[40m'+texto+'\033[0;0m'
    texto = fundo_preto
    return texto
  if cor == 'fvermelho':
    fundo_vermelho = '\033[41m'+texto+'\033[0;0m'
    texto = fundo_vermelho
    return texto
  if cor == 'fverde':
    fundo_verde = '\033[42m'+texto+'\033[0;0m'
    texto = fundo_verde
    return texto
  if cor == 'famarelo':
    fundo_amarelo = '\033[43m'+texto+'\033[0;0m'
    texto = fundo_amarelo
    return texto
  if cor == 'fazul':
    fundo_azul = '\033[44m'+texto+'\033[0;0m'
    texto = fundo_azul
    return texto
  if cor == 'fmagenta':
    fundo_magenta = '\033[45m'+texto+'\033[0;0m'
    texto = fundo_magenta
    return texto
  if cor == 'fciano':
    fundo_ciano = '\033[46m'+texto+'\033[0;0m'
    texto = fundo_ciano
    return texto
  if cor == 'fbranco':
    fundo_branco = '\033[47m'+texto+'\033[0;0m'
    texto = fundo_branco
    return texto
