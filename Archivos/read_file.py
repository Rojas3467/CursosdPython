#leer un archivo linea por linea
"""
with open('lectura y escritura de archivos/caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#leer todas las lineas en una lista
with open('lectura y escritura de archivos/caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    
#Añadir texto
"""with open('lectura y escritura de archivos/caperucita.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")"""