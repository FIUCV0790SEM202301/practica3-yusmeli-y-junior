#Aquiles, el famoso guerrero griego, entabla una carrera con una tortuga
distancia_AT = float(input("ingrese la distancia entre Aquiles y la tortuga (metros):"))
velocidad_T = float(input("ingrese un numero para la velocidad de la tortuga (m / h):"))
velocidad_A = (velocidad_T * 10)
alcance_AT= distancia_AT/(velocidad_A - velocidad_T)

opcion_1 = 0

while opcion_1!=3:
    print("""
    indique la opcion que desee
    1) horas, minutos y segundos
    2) colocar los datos
    3) salir
    """)

    opcion_1 = int(input())

    if opcion_1 == 1:
        print(" ")
        print("el tiempo que tardan en encontrarse Aquiles y la tortuga es:",int(alcance_AT*1),"horas",int((alcance_AT*60)%60),"minutos", int(alcance_AT*3600)%60,"segundos")
    if opcion_1 == 1:
     for i in range(1,6):
        distancia_aquiles = velocidad_A * (distancia_AT / (velocidad_A - velocidad_T) * (i/5))
        tiempo = (distancia_AT / (velocidad_A - velocidad_T) * (i/5))
        print("{} metros\t\t{} horas, {} minutos, {} segundos".format(distancia_aquiles,int(tiempo*1),int((tiempo*60)%60), int(tiempo*3600)%60 ))

    if opcion_1 == 2:
       distancia_AT = float(input("ingrese la distancia entre Aquiles y la tortuga (metros):"))
       velocidad_T = float(input("ingrese un numero para la velocidad de la tortuga (m / h):"))
       velocidad_A = (velocidad_T * 10)
       alcance_AT= distancia_AT/(velocidad_A - velocidad_T)
       print(" ")
       print("el tiempo que tardan en encontrarse Aquiles y la tortuga es:", "horas",int(alcance_AT*1),"minutos",int((alcance_AT*60)%60), "segundos", int(alcance_AT*3600)%60)
    if opcion_1 == 2:
     for i in range(1,6):
        distancia_aquiles = velocidad_A * (distancia_AT / (velocidad_A - velocidad_T) * (i/5))
        tiempo = (distancia_AT / (velocidad_A - velocidad_T) * (i/5))
        print("{} metros\t\t{} horas, {} minutos, {} segundos".format(distancia_aquiles,int(tiempo*1),int((tiempo*60)%60), int(tiempo*3600)%60 ))

    if opcion_1 == 3:
        print("ESPERO LE HAYA SIDO DE MUCHA AYUDA")
        break