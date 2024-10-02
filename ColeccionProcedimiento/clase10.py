numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Nidia",
               "Apellido": "Rojas",
               "Altura": 1.56,
               "Edad": 22}
print(information)
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Nidia": {"Apellido": "Rojas",
               "Altura": 1.56,
               "Edad": 22},
            "Odelkis": {"Apellido": "Mendoza",
               "Altura": 1.50,
               "Edad": 21}}
print(contacts["Nidia"])