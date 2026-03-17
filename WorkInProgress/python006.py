import json

dados = {"nome": "Padawan", "nivel": "iniciante"}
with open("dados.json", "w") as f:
    json.dump(dados, f, indent=2)

print("Salvo!")
