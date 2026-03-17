def fatores_primos(n):
    fatores = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            fatores.append(d)
            n //= d
        d += 1
    if n > 1:
        fatores.append(n)
    return fatores

print(fatores_primos(84))  # [2, 2, 3, 7]