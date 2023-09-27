# anotar los datos que necesitamos calcular lo que tarda otros cursos
# Ejercicio A promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Ejercicio B duracion de crudo
crudo_promedio = 5
crudo_dalto = 3.5

# Ejercicio A mostrar las diferencias de duracion
diferencias_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencias_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencias_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

# Ejercicio B calculando el porcentaje de tiempo vacio:
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

# mostrando las diferencias de duracion (ejercicio A)
print('----------')
print('El curso de Dalto dura:')
print(
    f' - un {diferencias_con_min}% menos que el más rapido')  # 40 %
print(
    f' - un {diferencias_con_max}% menos que el más lento')  # 40 %
print(
    f' - un {diferencias_con_promedio}% menos que el promedio')  # 40 %
print('----------')
# m ostrando la cantidad de espaciosvacios que se quitan (ejercicio B)
print(
    f'*********Un curso medio dura un {tiempo_vacio_promedio}% de tiempo vacío')  # 40 %
print(
    f'*********El curso de Dalto dura un {tiempo_vacio_dalto}% de tiempo vacío')  # 40 %
print('----------')
# mostrando diferencias si los cursos duraran 10 horas
print(
    f'Ver 10 horas de este curso equivale a {otros_cursos_promedio*100 // dalto_curso / 10}')  # redondeamos con // y * 10 cuantos ceros se añade muestra en decimales
