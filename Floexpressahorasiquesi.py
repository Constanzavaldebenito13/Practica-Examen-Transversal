#diccionarios

#diccionario descriptivo
arreglos={
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],

   'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],

   'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],

   'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],

   'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],

   'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],

}

#diccionario operativo

bodega = {

   'FLO1': [15990, 8],

   'FLO2': [29990, 3],

   'FLO3': [9990, 12],

   'FLO4': [24990, 5],

   'FLO5': [19990, 0],

   'FLO6': [22990, 6],

}

#validaciones diccionario descriptivo

def validar_nombre_del_arreglo(arreglo):
    if arreglo.strip()!="":
        return True
    else:
        return False

def validar_tipo_arreglo(tipo):
    if tipo.strip()!="":
        return True
    else:
        return False

def validar_Color_principal(color_principal):
    if color_principal.strip()!="":
        return True
    else:
        return False

def valida_tamaño_Del_arreglo(tamaño):
    if tamaño.strip().upper() in ["S","M","L"]:
        return True
    else:
        return False

def validar_tarjeta_dedicatoria(incluye_tarjeta):
    opcion=incluye_tarjeta.strip().lower()
    if opcion =="s":
        return True
    elif opcion=="n":
        return False
    else:
        return None

def validar_temporada_disponible(temporada):
    if temporada.strip()!="":
        return True
    else:
        return False

#validacion diccionario operativo

def valida_precio_de_venta(precio):
    if precio >0:
        return True
    else:
        return False

def validar_unidades_bodega(unidades):
    if unidades >=0:
        return True
    else:
        return False

#funcionamiento

def unidades_tipo(tipo):
    buscar_tipo=tipo.strip().lower()
    tipo_disponible=0

    for codigo in bodega:
        if codigo in arreglos and arreglos[codigo][1]==buscar_tipo:
            tipo_disponible+=bodega[codigo][1]
    print(f"La cantidad de arreglos por tipo {tipo} es de: {tipo_disponible}. ")

def busqueda_precio(p_min,p_max):
    resultados=[]

    for codigo in bodega:
        precio=bodega[codigo][0]
        disponibilidad=bodega[codigo][1]

        if p_min <=precio <=p_max and disponibilidad !=0:
            nombre=arreglos[codigo][0]
            resultados.append(nombre+"--"+codigo)
    resultados.sort()

    if len(resultados)==0:
        print("No hay arreglos en este rango de precio.")
    else:
        print(resultados)

def actualizar_precio(codigo,nuevo_precio):
    codigo=codigo.strip().upper()

    if not codigo in bodega:
        return False
    
    bodega[codigo][0]=nuevo_precio
    print("Precio actualizado")
    return True

def agregar_arreglo(codigo,nombre,tipo,color_principal,tamaño,incluye_tarjeta,temporada,precio,unidades):
    codigo=codigo.strip().upper()

    if codigo in bodega:
        print("El codigo ya existe")
        return False

    if not validar_nombre_del_arreglo(nombre):
        print("Error: Nombre de arreglo invalido")
        return False

    if not validar_tipo_arreglo(tipo):
        print("Error: Tipo de arreglo invalido")
        return False

    if not validar_Color_principal(color_principal):
        print("Error: Color principal invalido")
        return False

    if not valida_tamaño_Del_arreglo(tamaño):
        print("Error: Tamaño invalido solo se permite S,M,L")
        return False

    incluye_tarjeta_booleano=validar_tarjeta_dedicatoria(incluye_tarjeta)
    if incluye_tarjeta_booleano is None:
        print("Error: Respuesta invalida (Debe ser 's' o 'n')")
        return False

    if not validar_temporada_disponible(temporada):
        print("Error: Temporada invalida")
        return False

    if not valida_precio_de_venta(precio):
        print("Error: El precio debe ser un numero entero mayor a 0.")
        return False

    if not validar_unidades_bodega(unidades):
        print("Error: Las unidades disponibles deben ser un numero entero igual o mayor a 0")
        return False

    arreglos[codigo]=[nombre.strip().lower(),tipo.strip().lower(),color_principal.strip().lower(),tamaño.strip().upper(),incluye_tarjeta_booleano,temporada.strip().lower()]
    bodega[codigo]=[precio,unidades]
    print("Arreglo agregado")

def eliminar_arreglo(codigo):
    codigo=codigo.strip().upper()
    if codigo in arreglos and codigo in bodega:
        del arreglos[codigo]
        del bodega[codigo]
        print("Arreglo eliminado")
        return True
    else:
        print("El codigo no existe")
        return False

#menu

def mostrar_menu():
    print()
    print("=====MENU PRINCIPAL=====")
    print("1. Unidades por arreglo")
    print("2. Busqueda de arreglos por rango de precios")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar Arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("===========================")

#leer opciones

def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opcion: "))
            if opcion >=1 and opcion <=6:
                return opcion
            else:
                print("Error: Seleccione una opcion valida: ")
        except ValueError:
            print("Solo se permite un numero entero positivo")

#opcioneeeeeeeees

while True:
    mostrar_menu()
    opcion=leer_opcion()

    if opcion==1:
        tipo=input("Ingrese el tipo de arreglo: ")
        unidades_tipo(tipo)

    elif opcion==2:
        try:
            p_min=int(input("Ingrese el precio minimo: "))
            p_max=int(input("Ingrese el precio maximo: "))

            if p_min >=0 and p_max >=p_min:
                busqueda_precio(p_min,p_max)
            else:
                print("Error: Rango de precio invalido")
        except ValueError:
            print("El precio debe ser un numero entero")

    elif opcion==3:
        codigo=input("Ingrese el codigo")
        try:
            precio=int(input("Ingrese el precio a actualizar: "))
            actualizar_precio(codigo,precio)
        except ValueError:
            print("El precio debe ser un numero entero")

    elif opcion==4:
        print("====REGISTRAR NUEVO ARREGLO====")
        codigo=input("Ingrese el codigo de su arreglo: ").strip().upper()

        if codigo in arreglos:
            print("El codigo ya existe")
            continue

        nombre=input("Ingrese el nombre del arreglo: ").strip()
        tipo=input("Ingrese el tipo de arreglo: ").strip()
        color_principal=input("Ingrese el color principal: ").strip()
        tamaño=input("Ingrese el tamaño(S,M,L): ").strip().lower()
        incluye_tarjeta=input("Ingrese si el arreglo incluye tarjeta(s/n): ").strip().lower()
        temporada=input("Ingrese la temporada: ").strip()

        try:
            precio=int(input("Ingrese el precio del arreglo: "))
            unidades=int(input("Ingrese la cantidad de unidades disponibles: "))

            agregar_arreglo(codigo,nombre,tipo,color_principal,tamaño,incluye_tarjeta,temporada,precio,unidades)
        except ValueError:
            print("Error: El precio y las unidades deben ser un numero entero")

    elif opcion==5:
        codigo=input("Ingrese el codigo del producto a eliminar: ")

        eliminar_arreglo(codigo)

    elif opcion==6:
        print("Programa finalizado.")
        break
