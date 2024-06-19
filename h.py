

i=0

trabajador=["nombre          ","cargo          ","sueldobruto          ","Descuento Salud","Descuento AFP","Sueldo Liquido"]
trabajadores=[]

cantidad=0
menu=-1
while menu!=4:
    print("1.- Registar trabajador")
    print("2.- lista de todos los trabajadores")
    print("3.- imprimir plantilla de sueldo")
    print("4.- salir del programa")
    menu=int(input(">>> "))
    if menu==4:
        print("saliendo...")
    if menu==1:
        nombre=input("nombre y apellido: ")
        print("CARGO")
        print("1.-ceo")
        print("2.-desarrollador")
        print("3.-analista de datos")
        opcioncargo=int(input(">>>"))
        if opcioncargo==1:
            cargo="Ceo"
        if opcioncargo==2:
            cargo="Desarrollador"
        if opcioncargo==3:
            cargo="Analista de datos"
        sueldobruto=int(input("ingrese su sueldo bruto: "))

        cantidad=cantidad+1
        descuentosalud=70000
        descuentoafp=120000
        sueldoliquido=(sueldobruto-(descuentosalud+descuentoafp))
        trabajadores.append([nombre,cargo,sueldobruto,descuentosalud,descuentoafp,sueldoliquido])

        
    if menu==2:
        print(trabajador)
        while i < len(trabajadores):
            print(trabajadores[i])
            i=i+1
    if menu==3:
        with open("archivo.txt","w") as archivo:
            for trab in trabajadores:
                archivo.write(",".join(map(str,trab))+ "\n")