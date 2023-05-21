with open("key_skills2.csv", "r", encoding="utf8") as f:
    n = []
    for line in f.readlines():
        code = line.split("|")[0][:-2]
        n += ["(" +code + ", (" + line[:-1] + ")" + ")" ]
with open("key_skills3.csv", "w", encoding="utf8") as f:
    f.write(";\n".join(n))