def frase(nombre, apellido, adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'


# si cambia el apellido delante
frase_resultante = frase("Rivera", "Inma", "imbecil")
print(frase_resultante)

# forzandolo
frase_resultante = frase(apellido="Rivera", nombre="Inma",
                         adjetivo="imbecil")  # no cambia

print(frase_resultante)  # no cambia
