import random

print("bem vindo ao jogo de adivinhação!")

numero_secreto = random.randrange(1, 101)
tentativa = 0
pontos = 1000

print("qual nivel da dificuldade?")
print("(1) facil (2) medio (3) dificil")

nivel = int(input("defina o nivel: "))

if(nivel == 1):
    tentativa = 20
elif(nivel == 2):
    tentativa = 10
else:
    tentativa= 5

for rodada in range(1, tentativa + 1):
    print("tentativa {} de {}".format(rodada, tentativa))

    chute_str = input("digite um número entre 1 e 100: ")
    print("você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("você errou! o seu chute foi maior do que o número secreto.")
        elif(menor):
            print("você errou! o seu chute foi menor do que o número secreto.")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos    

print("fim do jogo")