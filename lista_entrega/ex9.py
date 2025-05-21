import random

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

random.shuffle(alfabeto)

letra = input("Digite uma letra do alfabeto: ").lower()
palpite = int(input(f"Em qual posição (de 0 a 25) você acha que a letra '{letra}' está? "))

if alfabeto[palpite] == letra:
    print("✅ Você acertou!")
else:
    print(f"❌ Você errou. A letra '{letra}' está na posição {alfabeto.index(letra)}.")
