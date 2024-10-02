import csv

#Leer un archivo
"""with open('Archivos/nidia/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)"""

#Mostrar la informaciòn por columnas
with open('Archivos/nidia/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")
