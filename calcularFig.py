
import pandas as pd
from figuras import rectangulo, circulo, triangulo

df = pd.read_csv("figuras.csv")
print("El archivo ha sido leido")

resultados = []

for index, row in df.iterrows():
    fig = str(row["FIGURA"]).strip().lower()
    m1 = float(row["MEDIDA1"])
    m2 = float(row["MEDIDA2"])

    if fig == "c":
        area, per = circulo(m1)
        figura_txt = "circulo"
    elif fig == "r":
        area, per = rectangulo(m1, m2)
        figura_txt = "rectangulo"
    elif fig == "t":
        area, per = triangulo(m1, m2)
        figura_txt = "triangulo"
    else:
        print(f"Fila {index}: FIGURA desconocida {row['FIGURA']}")
        continue

    print(f"Fila {index}: {figura_txt} -> AREA={area:.6f}, PERIMETRO={per:.6f}")
    resultados.append([figura_txt, m1, m2, round(area, 6), round(per, 6)])

pd.DataFrame(
    resultados,
    columns=["FIGURA", "MEDIDA1", "MEDIDA2", "AREA", "PERIMETRO"]
).to_csv("resultados.csv", index=False)

print(f"\nListo: resultados.csv con {len(resultados)} filas.")

