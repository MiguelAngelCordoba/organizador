def criterio(x):
    if x > 1440:
        print("Un dia solo tiene 24 horas (1440 minutos)")
    elif x < 1440 and x > 480:
        print("Genial, has aprovechado mas de 8 horas de tu dia")
    else:
        print("Esfuerzate mas, has aprovechado menos de 8 horas en el dia")