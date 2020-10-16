import json

candFile = open("candidatos.json", "r")
colFile = open("colocados.json", "r")
candidatos = json.load(candFile)
colocados = json.load(colFile)
candFile.close()
colFile.close()

final = []
for name in colocados:
    i = 0
    candidato = candidatos[0]
    while (name != candidato['name']):
        i += 1
        candidato = candidatos[i]
    final.append(candidato)

final.sort(key=lambda o: o['grade'])
fp = open("lcc.json", "w")
json.dump(final, fp, indent=0, ensure_ascii=False)
print(len(final))