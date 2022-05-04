import cores
def madlib():
  adjetivo = input("Adjetivo: ")
  adjetivo = cores.mudaCor(adjetivo, 'azul')
  verbo1 = input("Verbo: ")
  verbo1 = cores.mudaCor(verbo1, 'amarelo')
  verbo2 = input("Verbo: ")
  verbo2 = cores.mudaCor(verbo2, 'vermelho')
  alguem_famoso = input("Alguém Famoso: ")
  alguem_famoso = cores.mudaCor(alguem_famoso, 'verde')
  madlib = f"Programação computacional é tão {adjetivo}! Me deixa tão excitado pois, eu amo {verbo1}. Fique Hidratado e {verbo2} como se você fosse {alguem_famoso}!"
  print(madlib)

#  print("""
 # Meu Amigo Famoso!

  #Hoje é _Dia da Semana_ e eu estou muito _Sentimento_. Na verdade eu gostaria que fosse _Data Especial_ Para que eu pudesse _Verbo_ e _Verbo_.
  #Tenho um amigo famoso, _Adjetivo no diminutivo_ e nós sempre vamos ao _Local_. Quando estamos lá, nós gostamos de _Verbo_ no _Substantivo comum_
  #""")

madlib()


#def jogo():
 # continua = 1
  #while continua != 1:
   # print("""
    #  Vamos jogar MadLibs
    #""")