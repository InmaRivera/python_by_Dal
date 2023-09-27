es_igual_que = 5 == 6  # False
distinto_de = 5 != 6  # true
mayor_que = 5 > 6  # false
menor_que = 5 < 6  # true
mayor_o_igual = 5 >= 6  # false
menor_o_igual = 5 <= 6  # true

print(menor_o_igual)

# calculos combinados
a = 5
b = 10
c = 20
comparacion = a + b < c

# comparar usuarios
usuarios_de_base_de_datos = "Inma Rivera"
usuario_escrito = "Inma"
# si la contraseña no coincide sale False y no deja pasar
contraseña_almacenada = "InmaRivera"
contraseña_escrita = "InmaRivera"

if contraseña_almacenada == contraseña_escrita:
    print('iniciando sesión')
else:
    print('contraseña erronea')
