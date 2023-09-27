# if True:
#     #accion se ejecuta
# else False:
#     #la accion no se ejecuta

edad = 17
if edad >= 18:
    print("puedes pasar")
    # todo lo que este aqui dentro forma parte del if es un lenguaje indentado
else:
    print("no puedes pasar")


# con contraseña
contraseña_real = "SoyInma"
contraseña_escrita = "Soyinma"

if contraseña_real == contraseña_escrita:
    print("iniciando sesión")
else:
    print("contraseña erronea")


# otra opcion
ingreso_mensual = 12000
gasto_mensual = 13000  # si gasta más de lo q gana estas en deficit, si gasta casi lo mismo gasta mucho y si tiene un gasto normal estas bien
if ingreso_mensual > 10000:
    print("estas bien en cualquier parte del mundo")
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien")
    else:
        print("gastas mucho")

elif ingreso_mensual > 1000:  # elif para el else if
    print("estas bien en España")
else:
    print("eres pobre")
