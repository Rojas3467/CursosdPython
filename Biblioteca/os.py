import os

#Obtener el directorio actual
"""cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)"""

#listar los archivos.txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)

os.rename('caperucita.txt', 'cuento.txt')
print('Atchivo renombrado')

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)