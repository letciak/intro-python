import forca
import adivinhacao

def escolhe_jogo():

    print("escolha seu jogo: (1) forca ou (2) adivinhacao")

    jogo = input(int("qual jogo? "))

    if (jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("jogando adivinhacao")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()