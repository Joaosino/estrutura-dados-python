import random


def chute(x):
    randomico = random.randint(1, x)
    chute = 0
    while chute != randomico:
        chute = int(input(f'escolha um número entre 1 e {x}: '))
        if chute < randomico:
            print("Desculpe, tente novamente. Muito baixo!")
        elif chute > randomico:
            print("Desculpe, tente novamente. Muito alto.")
    print(f"Acerto misevaví! você chutou o número {chute} corretamente!")


def chuteDoPc(x):
    minimo = 1
    maximo = 10
    feedback = ''
    while feedback != 'c':
        chute = random.randint(minimo, maximo)
        feedback = input(
            f"Chutei o número {chute}, foi muito alto?(A), Baixo?(B) ou correto?(C)").lower()
        if feedback == 'h':
            maximo = chute - 1


def jogo():
    continua = 1
    while continua != 0:
        print("""
    
    Vamos jogar Adivinhe o número!
    Primeiro você irá adivinhar um número entre 1 e 10 e eu irei te dizer se está ou não próximo ou certo!
    depois inverteremos os papeis e eu adivinharei!

    
    """)
        continua = int(
            input("deseja continuar? 1 para sim e 0 para voltar ao menu! "))
        if continua == 1:
            chute(10)
            chuteDoPc(10)
        else:
            import menuAps
            menuAps.menuInicial()


jogo()
