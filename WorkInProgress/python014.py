import zipfile

with zipfile.ZipFile("backup.zip", "w") as z:
    z.write("dados.json")