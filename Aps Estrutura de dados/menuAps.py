def menuDeJogos(escolha):
    if escolha == 0:
        print('Obrigado por ter jogado nosso jogo!')
        quit()
    if escolha == 1:
        import blackJack
        blackJack.jogo()
    if escolha == 2:
        import adivinheONumero
        adivinheONumero.jogo()
    if escolha == 3:
        import madlib
        madlib.madlib()
    if escolha == 4:
        return


def menuInicial():
    print("""

    Olá, eu sou o navegador de jogos! aqui você poderá escolher entre 4 opções sendo elas BlackJack, Adivinhe o Número, MadLibs e outro que ainda não existe

    escolha um jogo para começar ou aperte o 0 para terminar a aplicação!

    (1)BlackJack
    (2)Adivinhe o número
    (3)MadLibs
    (0)Encerrar a aplicação
      
      """)
    escolha = int(input("escolha: "))
    menuDeJogos(escolha)


menuInicial()
