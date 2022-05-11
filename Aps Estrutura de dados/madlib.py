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
    madlib = f"Programação computacional é tão {adjetivo}! Me deixa tão excitado pois, eu amo {verbo1}. Fique Hidratado e vá {verbo2} como se você fosse {alguem_famoso}!"
    print(madlib)
    print('Este foi um exemplo do que vem a seguir!')

    print("""
Meu Amigo Famoso!
Hoje é _Dia da Semana_ e eu estou muito _Sentimento_. Na verdade eu gostaria que fosse _Data Especial_ Para que eu pudesse _Verbo_ e _Verbo_.
Tenho um amigo famoso, _Adjetivo no diminutivo_ e nós sempre vamos ao _Local_. Quando estamos lá, nós gostamos de _Verbo_ no _Substantivo comum_
""")

    dia_da_semana = str(input('Dia da Semana: '))
    sentimento = str(input('Sentimento: '))
    data_especial = str(input('Data especial: '))
    verbo1 = str(input('verbo: '))
    verbo2 = str(input('verbo: '))
    adjetivo_no_diminutivo = str(input('Adjetivo no diminutivo: '))
    local = str(input('Local: '))
    verbo3 = str(input('Verbo: '))
    substantivo_comum = str(input('Substantivo Comum: '))

    print(f"""
Meu Amigo Famoso!
Hoje é {dia_da_semana} e eu estou muito {sentimento}. Na verdade eu gostaria que fosse {data_especial} Para que eu pudesse {verbo1} e {verbo2}.
Tenho um amigo famoso, {adjetivo_no_diminutivo} e nós sempre vamos ao {local}. Quando estamos lá, nós gostamos de {verbo3} no {substantivo_comum}
""")

    print("gostou? se quiser tentar novamente digite 1, senão digite 0")
    escolha = int(input("escolha: "))
    if escolha == 1:
        madlib()
    else:
        import menuAps
        menuAps.menu()
