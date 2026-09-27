#códigos do dia 24

import random

while True:
    print("=== JOGO DE ADIVINHAÇÃO ===")
    limite = int(input("Escolha o nível (10, 20 ou 30): "))

    numero = random.randint(1, limite)

    for tentativa in range(3):
        palpite = int(input("Digite seu palpite: "))

        if palpite == numero:
            print("Parabéns, você acertou!")
            break
        elif palpite < numero:
            print("Você errou! Tente um número maior.")
        else:
            print("Você errou! Tente um número menor.")

    else:
        print("Você perdeu! Fim de jogo.")
        print("O número era:", numero)

    novamente = input("Quer jogar novamente? (s/n): ")

    if novamente != "s":
        break