import secrets, string

alfabeto = string.ascii_letters + string.digits + "!@#$%"
senha = ''.join(secrets.choice(alfabeto) for _ in range(12))
print(senha)