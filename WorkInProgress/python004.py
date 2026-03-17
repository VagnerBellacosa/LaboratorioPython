lista = [10, 20, 30, 20, 40, 20]
indices = [i for i, v in enumerate(lista) if v == 20]
print(indices)  # [1, 3, 5]