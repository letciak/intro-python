def jogar():

    print("bem vindo ao jogo da forca!")

    palavra_secreta = "python"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("letra {} na posição {}".format(letra, index))
            index = index + 1

        print("jogando")

    print("fim do jogo")

if (__name__ == "__main__"):
    jogar()
