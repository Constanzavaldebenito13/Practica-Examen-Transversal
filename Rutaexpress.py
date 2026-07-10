#diccionarios

#diccionario descriptivo

recorridos = {
'R001': ['Santiago', 'Valparaiso', 120, 'normal', 'dia', True],
'R002': ['Santiago', 'Concepcion', 500, 'cama', 'noche', True],
'R003': ['La Serena', 'Coquimbo', 15, 'normal', 'dia', False],
'R004': ['Temuco', 'Valdivia', 165, 'semi-cama', 'dia', True],
'R005': ['Iquique', 'Arica', 310, 'cama', 'noche', False],
'R006': ['Santiago', 'Rancagua', 90, 'normal', 'dia', True]
}

#diccionario operativo
venta = {
'R001': [7990, 20],
'R002': [25990, 0],
'R003': [1990, 35],
'R004': [12990, 8],
'R005': [18990, 3],
'R006': [4990, 12]
}

#validacion diccionario descriptivo

def validar_ciudad_origen(origen):
    if origen.strip()!="":
        return True
    else:
        return False

def validar_ciudad_destino(destino):
    if destino.strip()!="":
        return True
    else:
        return False

def validar_distancia_total(distancia_km):
    if distancia_km >0:
        return True
    else:
        return False

def validar_tipo_de_bus(tipo_bus):
    if tipo_bus.strip().lower() in ["normal","semi-cama","cama"]:
        return True
    else:
        return False

def validar_turno_del_servicio(servicio):
    if servicio.strip().lower() in ["dia","noche"]:
        return True
    else:
        return False

def wifi_a_bordo(tiene_wifi):
    opcion=tiene_wifi.strip().lower()
    if opcion=="s":
        return True
    elif opcion == "n":
        return False
    else:
        return None

#validacion diccionario operativo
def precio_del_pasaje(precio):
    if precio >0:
        return True
    else:
        return False

def asientos_disponibles(asientos):
    if asientos >=0:
        return True
    else:
        return False

#Menu y opcion
def mostrar_menu():
    print()
    print("=======MENU PRINCIPAL========")
    print("1. Asientos por cuidad de origen")
    print("2. Busqueda de recorridos por rango de precio")
    print("3. Actualizar precio de recorrido")
    print("4. Agregar recorrido")
    print("5. Eliminar recorrido")
    print("6. Salir")
    print("=================================")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opción: "))
            if opcion >=1 and opcion <=6:
                return opcion 
            else:
                print("Debe seleccionar una opción válida.")
        except ValueError:
            print("Error: Solo se permite un numero entero positivo.")

def asientos_origen(origen):
    tipo_buscar=origen.strip().lower()
    total_asientos=0

    for codigo in venta:
        if codigo in recorridos and recorridos[codigo][0]==tipo_buscar:

            total_asientos+=venta[codigo][1]

    print(f"El total de asientos es de: {total_asientos}")

def busqueda_precio(p_min, p_max):
    resultados=[]
    for codigo in venta:
        precio=venta[codigo][0]
        disponible=venta[codigo][1]

        if p_min <=precio <=p_max and disponible !=0:
            nombre=recorridos[codigo][0]
            resultados.append(nombre+"--"+codigo)
    resultados.sort()

    if len(resultados)==0:
        print("No hay reccoridos en este rango de precio")
    else:
        print(resultados)

def actualizar_precio(codigo,precio_nuevo):
    codigo=codigo.strip().upper()
    if not codigo in venta:
        return False
    venta[codigo][0]=precio_nuevo
    return True

def agregar_recorrido(codigo,origen,destino,distancia,tipo_bus,servicio,tiene_wifi,precios,asientos):
    codigo=codigo.strip().upper()

    if codigo in recorridos:
        print("El codigo ya existe")
        return False

    if not validar_ciudad_origen(origen):
        print("Error: Ciudad de origen invalida")
        return False

    if not validar_ciudad_destino(destino):
        print("Error: Ciudad de destino invalida")
        return False

    if not validar_distancia_total(distancia):
        print("Error: La distancia debe ser mayor a 0")
        return False

    if not validar_tipo_de_bus(tipo_bus):
        print("Error: Tipo invalido")
        return False

    if not validar_turno_del_servicio(servicio):
        print("Error: Turno invalido")
        return False

    tiene_wifi_booleano=wifi_a_bordo(tiene_wifi)
    if tiene_wifi_booleano is None:
        print("Error: Respuesta de wifi invalida(Debe ser 's' o 'n').")
        return False

    if not precio_del_pasaje(precios):
        print("Error: El precio debe ser mayor a 0")
        return False

    if not asientos_disponibles(asientos):
        print("Error: La cantidad de asientos debe ser igual o mayor a 0.")
        return False

    recorridos[codigo]=[origen.strip(),destino.strip(),distancia,tipo_bus.strip().lower(),servicio,tiene_wifi_booleano]   
    venta[codigo]=[precios,asientos]
    print("Recorrido Agregado")
    return True

def eliminar_recorrido(codigo):
    codigo=codigo.strip().upper()

    if codigo in recorridos and codigo in venta:
        del recorridos[codigo]
        del venta[codigo]
        print("Plan eliminado")
        return True
    else:
        print("Codigo no existe")
        return False

while True:
    mostrar_menu()

    opcion=leer_opcion()

    if opcion==1:
      origen=input("Ingrese la ciudad de origen")
      asientos_origen(origen)

    elif opcion==2:
        try:
            p_min=int(input("Ingrese el precio minimo"))
            p_max=int(input("Ingrese el precio maximo"))
            if p_min >=0 and p_max >=p_min:
                busqueda_precio(p_min,p_max)
            else:
                print("Error: Rango de precios invalidos")
        except ValueError:
            print("Ingrese valores numericos enteros")

    elif opcion==3:
        codigo=input("Ingrese el codigo del recorido(ej. R001)").strip().upper()
        try:
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            actualizar_precio(codigo, nuevo_precio)
        except ValueError:
            print("Error: El precio debe ser un número entero.")
                
    elif opcion == 4:
        print("\n--- Registrar Nuevo Recorrido ---")
        codigo = input("Código (ej. R007): ").strip().upper()
        if codigo in recorridos:
            print("El código ya existe.")
            continue
                
        origen = input("Ciudad de origen: ").strip()
        destino = input("Ciudad de destino: ").strip()
            
        try:
            distancia = int(input("Distancia en KM: "))
            tipo_bus = input("Tipo de bus (normal / semi-cama / cama): ").strip()
            servicio = input("Turno del servicio (dia / noche): ").strip()
            wifi_input = input("¿Tiene WiFi? (s/n): ").strip().lower()
            precio = int(input("Precio del pasaje: "))
            asientos = int(input("Asientos disponibles: "))
                
               
            agregar_recorrido(codigo, origen, destino, distancia, tipo_bus, servicio, wifi_input, precio, asientos)
        except ValueError:
            print("\nError: Distancia, precio y asientos deben ser números enteros.")
                
    elif opcion == 5: 
        codigo = input("Ingrese el código del recorrido a eliminar (ej. R001): ")
        eliminar_recorrido(codigo)
        
    elif opcion == 6: 
        print("Programa finalizado.")
        break
                 