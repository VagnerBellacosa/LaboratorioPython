import csv

with open("a.csv") as f1, open("b.csv") as f2, open("saida.csv", "w", newline="") as out:
    r1, r2 = csv.reader(f1), csv.reader(f2)
    w = csv.writer(out)

    for l1, l2 in zip(r1, r2):
        w.writerow(l1 + l2)