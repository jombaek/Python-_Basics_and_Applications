res = []

with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
    for line in fin:
        res.append(line.strip())
    for i in range(len(res) - 1, -1, -1):
        fout.write(res[i] + "\n")
