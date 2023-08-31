"""Jogo da Forca utilizando listas"""

from random import choice



palavras = ["banana", "pastel", "borboleta", "machado", "morango", "futebol"]
palavra_secreta = choice(palavras)
letras_acertadas = []
sentenca = ""

for letra in palavra_secreta:
    letras_acertadas.append("_")

Title(f'Bem vindo(a) ao jogo da forca!')
print(f'\033[0;32mA palavra é:\033[m')
for word in letras_acertadas:
    sentenca += word
print(sentenca)
chances = 6

while True:
    chute = input("Qual letra? ").lower()[0]
    if not chute.isalpha():
        print(f'\033[0;31mPor favor, digite uma letra!\033[m')
    else:
        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if chute.lower() == letra.lower():
                    letras_acertadas[posicao] = letra
                posicao = posicao + 1
            print(f'{chances} chances disponíveis')
            sentenca = ""
            for word in letras_acertadas:
                sentenca += word
            print(sentenca.upper())

        if chute not in palavra_secreta:
            chances -= 1
            print(f'\033[0;31mVocê Errou!\033[m')
            print(f'\033[0;36m{chances} chances disponíveis\033[m')
            sentenca = ""
            for word in letras_acertadas:
                sentenca += word
            print(sentenca.upper())

        if chances == 0:
            print(f'\033[0;31mVocê perdeu :(\033[m')
            print()
            break

        if "_" not in letras_acertadas:
            print(f'\033[0;35mParabéns, você ganhou!\033[m')
            break
