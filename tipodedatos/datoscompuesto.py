# la lista va con corchetes []
lista = ["Conchi Rivera", "Soy Rivera", True, 1.70]

# las tuplas va con parentesis ()
tupla = ["Inma Rivera", "Soy Rivera", True, 1.70]
lista[1] = "jakoooo"  # la lista se puede modificar, las tuplas no
tupla [0] ="luna"
print(lista[1])
print(tupla[0])  # soy rivera, en programacion empieza por 0 siempre

#creando un conjunto (set)
#no se puede llamar a elementos por indices, no se puede almacenar elementos duplicados
conjunto = {"Inma Rivera", "Soy Rivera", True, 1.70}
#conjunto = {"jajaja maquina te jodi"}
print(conjunto)

#creando un diccionario o dict, como el json de js, es key : value
diccionario ={
    'nombre': "Inma Rivera",
    'canal': "inma",
    'esta_emocionado': True,
    'altura': 1.70
}
print(diccionario['altura']+3)