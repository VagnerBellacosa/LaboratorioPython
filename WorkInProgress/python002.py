def eh_palindromo(texto):
    t = ''.join(c.lower() for c in texto if c.isalnum())
    return t == t[::-1]

print(eh_palindromo("A base do teto desaba"))  # True