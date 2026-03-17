def valido(tab, r, c, n):
    for i in range(9):
        if tab[r][i] == n or tab[i][c] == n:
            return False
    br, bc = 3*(r//3), 3*(c//3)
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if tab[i][j] == n:
                return False
    return True

def resolver(tab):
    for r in range(9):
        for c in range(9):
            if tab[r][c] == 0:
                for n in range(1, 10):
                    if valido(tab, r, c, n):
                        tab[r][c] = n
                        if resolver(tab):
                            return True
                        tab[r][c] = 0
                return False
    return True