frase = "Python é poderoso e elegante"
palavras = frase.split()
ordenadas = sorted(palavras, key=str.lower)
print(ordenadas)