palavra = "python"
letras = set(palavra)
tentativas = 6
usadas = set()

while tentativas > 0 and letras:
    print("Palavra:", ' '.join(c if c in usadas else '_' for c in palavra))
    chute = input("Letra: ").lower()

    if chute in letras:
        letras.remove(chute)
    else:
        tentativas -= 1

    usadas.add(chute)

print("Você venceu!" if not letras else "Game Over")