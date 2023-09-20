print("bem vindo ao jogo de Adivinhação!")

numero_secreto = 42

chute_str = input("digite o seu número: ")
print("você digitou " , chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("parabéns! você acertou!")
else:
    if(maior):
        print("o seu chute foi maior do que o número secreto!")
    elif(menor):
        print("o seu chute foi menor do que o número secreto!")

print("fim do jogo")