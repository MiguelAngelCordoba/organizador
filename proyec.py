# Programa para administrar el tiempo cada dia

def run():

    actividades = {}
    x = int(input("Cuantas actividades realizaste el dia dia de hoy = "))

    for i in range(x):
        y = input(f"La actividad numero {i+1} que realizaste hoy es = ")
        z = input("Cuanto tiempo en minutos utilizaste en esta actividad = ")
        actividades.update({y:z})
    
    print(actividades)


if __name__ == "__main__":
    run()