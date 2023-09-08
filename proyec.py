# Programa para administrar el tiempo cada dia

import fun
def run():

    actividades = {}
    x = int(input("\nCuantas actividades utiles realizaste el dia de hoy = "))

    for i in range(x):
        y = input(f"La actividad numero {i+1} que realizaste hoy es = ")
        z = int(input("Cuanto tiempo en minutos utilizaste en esta actividad = "))
        actividades.update({y:z})

    min_total = sum(actividades.values())
    fun.criterio(min_total)

    if "estudiar" not in actividades :
        print("\nNo has registrado tiempo a estudiar, recuerda que es la actividad mas importante") 

if __name__ == "__main__":
    run()