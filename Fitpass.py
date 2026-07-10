#diccionarios

#diccionario descripctivo
planes = {
'F001': ['Plan Basico', 'mensual', 1, False, False, 'libre'],
'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
'F004': ['Plan Senior', 'trimestral', 3, True, False, 'manana'],
'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}

#diccionario operativo
inscripciones = {
'F001': [14990, 30],
'F002': [22990, 10],
'F003': [39990, 0],
'F004': [35990, 6],
'F005': [159990, 2],
'F006': [18990, 15]
}

#validacion diccionario descriptivo

def validar_nombre_del_plan(nombre_plan):
    if nombre_plan.strip()!="":
        return True
    else:
        return False

def validar_tipo_segun_duracion(tipo_duracion):
    if tipo_duracion.strip().lower() in ["mensual","trimestral","anual"]:
        return True
    else: 
        return False

def validar_duracion_del_pan(duracion_meses):
    if duracion_meses >0:
        return True
    else:
        return False

def validar_incluye_piscina(acceso_piscina):
    opcion=acceso_piscina.strip().lower()
    if opcion == "s":
        return True
    elif opcion == "n":
        return False
    else:
        return None

def validar_incluye_clases(incluye_clases):
    opcion=incluye_clases.strip().lower()
    if opcion == "s":
        return True
    elif opcion == "n":
        return False
    else:
        return None

def validar_franja_horaria(horario):
    if horario.strip()!="":
        return True
    else:
        return False

#validacion diccionario operativo

def validar_precio_mensual(precio):
    if precio >0:
        return True
    else:
        return False

def cupos_inscripcion(cupos):
    if cupos >=0:
        return True
    else:
        return False

#Menu y leer opcion

def mostrar_menu():
    print()
    print("======MENU PRINCIPAL======")
    print("1. Cupos por tipo de plan")
    print("2. Busqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("==========================")
    
def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opción: "))
            if opcion >=1 and opcion <=6:
                return opcion
            else:
                print("Debe seleccionar una opción válida.")
        except ValueError:
            print("Solo se permite un número entero positivo.")

#Funcionamiento de las cosas :D

def cupos_tipo(tipo):
    tipo_buscar=tipo.strip().lower()
    total_cupos=0
    
    for codigo in inscripciones:
        if codigo in planes and planes[codigo][1]==tipo_buscar:

            total_cupos+=inscripciones[codigo][1]

    print(f"El total de cupos por tipo '{tipo}' es: {total_cupos}")

def busqueda_precio(p_min, p_max):
    resultados=[]
    for codigo in inscripciones:
        precio=inscripciones[codigo][0]
        disponible=inscripciones[codigo][1]
        if p_min <=precio <=p_max and disponible !=0:
            nombre=planes[codigo][0]
            resultados.append(nombre + "--" + codigo)
            resultados.sort()

    if len(resultados)==0:
        print("No hay planes en ese rango de precios.")
    else:
        print(resultados)

def actualizar_precio(codigo, nuevo_precio):
    codigo=codigo.strip().upper()
    if codigo not in inscripciones:
        print("El codigo no existe")
        return False
    inscripciones[codigo][0]=nuevo_precio
    print("Precio actualizado")
    return True

def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos):
    codigo=codigo.strip().upper()

    if codigo in planes:
        print("El codigo ya existe")
        return False

    if not validar_nombre_del_plan(nombre):
        print("Error: Nombre inválido.")
        return False

    if not validar_tipo_segun_duracion(tipo):
        print("Error: Tipo inválido.")
        return False

    if not validar_duracion_del_pan(duracion):
        print("Error: La duración debe ser mayor a 0.")
        return False

    incluye_piscina_booleano = validar_incluye_piscina(acceso_piscina)
    if incluye_piscina_booleano is None:
        print("Error: Respuesta de piscina inválida. (Debe ser 's' o 'n').")
        return False

    incluye_clases_booleano= validar_incluye_clases(incluye_clases)
    if incluye_clases_booleano is None:
        print("Error: Respuesta de clases inválida. (Debe ser 's' o 'n').")
        return False
    
    if not validar_franja_horaria(horario):
        print("Error: Franja honoraria inválida.")
        return False

    if not validar_precio_mensual(precio):
        print("Error: El precio debe ser mayor a 0.")
        return False

    if not cupos_inscripcion(cupos):
        print("Error: Los cupos no pueden ser negativos.")
        return False

    planes[codigo]=[nombre.strip(),tipo.strip().lower(),duracion,incluye_piscina_booleano,incluye_clases_booleano,horario.strip()]
    inscripciones[codigo]=[precio,cupos]
    print("Plan agregado")
    return True

def eliminar_plan(codigo):
    codigo=codigo.strip().upper()
    if codigo in planes and codigo in inscripciones:
        del planes[codigo]
        del inscripciones[codigo]
        print("Plan eliminado")
        return True
    else:
        print("El codigo no existe")
        return False



while True:  
    mostrar_menu()
        
    opcion=leer_opcion()
    if opcion==1:
        tipo=input("Ingrese el tipo de plan(mensual,trimestral,anual): ")
        cupos_tipo(tipo)
        mostrar_menu()
    elif opcion==2:
        try:
            p_min=int(input("Ingrese el precio minimo"))
            p_max=int(input("Ingrese el precio maximo"))
            busqueda_precio(p_min,p_max)
        except ValueError:
            print("Los numeros deben ser valores enteros")

    elif opcion ==3:
        codigo=input("Ingrese el codigo a actualizar: ")
        try:
            nuevo_precio=int(input("Ingrese el nuevo precio: "))
            actualizar_precio(codigo,nuevo_precio)
        except ValueError:
            print("El numero debe ser un numero entero.")

    elif opcion == 4:
        print("\n--- REGISTRO DE NUEVO PLAN ---")
        codigo = input("Código del plan (Ej: F010): ")
        nombre = input("Nombre del plan: ")
        tipo = input("Tipo (mensual, trimestral, anual): ")
        try:
            duracion = int(input("Duración en meses: "))
            acceso_piscina = input("¿Incluye piscina? (s/n): ")
            incluye_clases = input("¿Incluye clases grupales? (s/n): ")
            horario = input("Franja horaria: ")
            precio = int(input("Precio mensual: "))
            cupos = int(input("Cupos iniciales: "))
                
            agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos)
        except ValueError:
            print("Error de entrada: Duración, precio y cupos deben ser números enteros.")
                
    elif opcion == 5:
        codigo = input("Ingrese el código del plan a eliminar: ")
        eliminar_plan(codigo)
            
    elif opcion == 6:
        print("Programa finalizado.")
        break


