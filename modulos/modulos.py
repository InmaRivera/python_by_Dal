# import modulo_saludar  # importamos la otra clase

# saludo = modulo_saludar.saludar("Inma")  # llamamos al modulo saludar
# print(saludo)  # lo imprimimos

# usamos as y es lo mismo que lo de arriba
# import modulo_saludar as msaludar  # importamos la otra clase

# saludo = msaludar.saludar("Inma")  # llamamos al modulo saludar
# print(saludo)  # lo imprimimos

from modulo_saludar import saludar, saludar_raro as s_extraño

saludo = saludar("Inma")  # llamamos al modulo saludar
saludo_raro = s_extraño("Fran")
print(saludo)  # lo imprimimos
print(saludo_raro)

# accedemos al nombre de este modulo
print(__name__)

# accedemos al nombre del modulo llamado
print(saludar.__name__)
