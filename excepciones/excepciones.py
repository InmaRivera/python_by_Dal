# creando funcion que suma numeros
def sumar_dos():
    # lo iniciamos en un bucle
    while True:
        # pedimos los numeros
        a = input("numero 1: ")
        b = input("numero 2: ")
        # intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
            break
        # si lanza una excepcion, pedirle que reingrese los datos
        except:
            print("Te pedí un número")
            # si todo salio bien termnamos el bucle
        else:
            break
        finally:
            print("Esto se ejecuta siempre")
    return resultado


print(sumar_dos())
