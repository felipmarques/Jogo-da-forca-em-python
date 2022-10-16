"Jogo da Forca básico utilizando listas"

from funções import Title
from random import choice

palavras = ["banana", "pastel", "borboleta", "machado", "morango", "futebol"]
palavra_secreta = choice(palavras)
letras_acertadas = []

for letra in palavra_secreta:
    letras_acertadas.append("_")

Title(f'\033[0;34mBem vindo ao jogo da forca!\033[m')
print(f'\033[0;32mA palavra é:\033[m')
print(letras_acertadas)
chances = 6

while True:
    chute = input("Qual letra? ").lower()
    if chute in palavra_secreta:
        posicao = 0
        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                letras_acertadas[posicao] = letra
            posicao = posicao + 1
        print(letras_acertadas)
        print(f'{chances} chances disponíveis')

    if chute not in palavra_secreta:
        chances -= 1
        print(f'\033[0;31mVocê Errou!\033[m')
        print(letras_acertadas)
        print(f'\033[0;36m{chances} chances disponíveis\033[m')

    if chances == 0:
        print(f'\033[0;31mVocê perdeu :(\033[m')
        print()
        break

    if "_" not in letras_acertadas:
        print(f'\033[0;35mParabéns, você ganhou!\033[m')
        break
