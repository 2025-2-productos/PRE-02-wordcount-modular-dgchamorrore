import os

def test_migracion():
    if not os.path.exists("data/output/results.tsv"):
        raise FileNotFoundError("El archivo results.tsv no existe.")

    results = {}
    with open("data/output/results.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines() # lectura por linea
        for line in lines:
            key, value = line.strip().split("\t")
            results[key] = value

    #assert results["computational"] == 3 #si no es igual a 3 es falso -> error
    #assert results["analytics"] == 5

    assert results.get("computational", 0) == "3" #si no es igual a 3 es falso -> error
    assert results.get("analytics", 0)  == "5"