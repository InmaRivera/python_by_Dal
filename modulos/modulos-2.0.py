# si el modulo estuviera dentro de una carpeta en la misma ruta
# si estuviera fuera
import paquete.saludar
import modulo_saludar as m_saludar
import sys
# import funciones_buenas.saludar
# print(funciones_buenas.saludar.saludar("Antonia"))

print(sys.path.append(
    "C:\\Users\\conch\\Desktop\\Curso de Python\\modulos\\funciones_buenas"))
print(m_saludar.saludar("Antonia 2"))


print(paquete.saludar.saludar("Ramona "))
