import blackJack
import adivinheONumero
import madlib

def escolheJogo() :
  print("""

    Olá, eu sou o navegador de jogos! aqui você poderá escolher entre 4 opções sendo elas Xadrez, Sudoku, adivinhe o número e outro que ainda não existe

    escolha um jogo para começar ou aperte o 0 para terminar a aplicação!

    (1)BlackJack
    (2)Adivinhe o número
    (3)MadLibs
    (4)Outro
    (0)Encerrar a aplicação
      
      """)
  escolha = int(input("escolha: "))
  print(escolha)
  if escolha == 0:
    print('Obrigado por ter jogado nosso jogo!')
    quit() 
  if escolha == 1:
    blackJack.main()
  if escolha == 2:
    adivinheONumero.main()
  if escolha == 3:
    madlib.main()
"""  if escolha == 4:
    outro.main()
"""


escolheJogo()




