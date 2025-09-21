
import pandas as pd
from figuras import rectangulo

df = pd.read_csv("figuras.csv")
print("El archivo ha sido leido")


for index, row in df.iterrows():
	print(f"Fila {index}: FIGURA={row['FIGURA']}, MEDIDA1={row['MEDIDA1']}, MEDIDA2={row['MEDIDA2']}")



a = rectangulo(10,5)
print(a)
