texto = "python python código mainframe python"
contagem = {}

for palavra in texto.split():
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)