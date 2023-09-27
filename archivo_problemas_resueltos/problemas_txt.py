# 2 listas una con nombres y otra con apellidos
nombres = ["Lucas", "Inna", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto", "Rivera", "Zing", "Dato", "Robetix"]
# Registrar esta informacion en un txt de forma optima
with open("archivo_problemas_resueltos\\nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------------\n")
     for n, a in zip(nombres, apellidos)]
