import random

aleatorio = random.randint(1, 10)

while True:
    numero_palpite = int(input("Adivinhe o número entre 1 e 10: "))

    if numero_palpite > aleatorio:
        print("Muito alto, tente novamente!")
    elif numero_palpite < aleatorio:
        print("Muito baixo, tente novamente!")
    else:
        print(f"Correto! O número é {numero_palpite}.")
        break