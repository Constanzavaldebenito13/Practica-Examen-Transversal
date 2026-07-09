#diccionarios

#diccionario descriptivo
peliculas={
    'P101': ['Luz de Otono', 'drama', 110, 'B', 'Espanol', False],
    'P102': ['Noche Neon', 'accion', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Espanol', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Espanol', True],
    'P105': ['Codigo Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficcion', 132, 'B', 'Ingles', False]
}

#diccionario operativo

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3]
}

#Validaciones diccionario descriptivo

def validar_titulo(nombre_pelicula):
    if nombre_pelicula.strip() !="":
        return True
    else:
        return False

def validar_genero(genero_cinematografico):
    if genero_cinematografico.strip() !="":
        return True
    else:
        return False

def validar_duracion_min(duracion_en_minutos):
    if duracion_en_minutos >0:
        return True
    else:
        return False

def validar_clasificacion(clasificacion_audiencia):
    if clasificacion_audiencia in ["A","B","C"]:
        return True
    else:
        return False

def validacion_idioma(idioma_original):
    if idioma_original.strip()!="":
        return True
    else:
        return False

def validacion_es_3d(formato_3D):
    if formato_3D =="s":
        return True
    elif formato_3D=="n":
        return False
    else:
        return None



#Validacion diccionario operativo

def validar_precio_positivo(precio_entradas):
    if precio_entradas >0:
        return True
    else:
        return False


def validar_cupos(cupos_disponibles):
    if cupos_disponibles >=0:
        return True
    else:
        return False

#Menu y opcion
def mostrar_menu():
    print()
    print("=======MENU PRINCIPAL=========")
    print("1. Cupos por genero")
    print("2. Busqueda de peliculas por rango de precio")
    print("3. Actualizar precio de pelicula")
    print("4. Agregar pelicula")
    print("5. Eliminar pelicula")
    print("6. Salir")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opción: "))
            if opcion >=1 and opcion <=6:
                return opcion
            else:
                print("Debe seleccionar una opción válida.")
        except ValueError:
            print("Solo se permiten un numero entero positivo.")

def cupos_genero(genero):
    total_cupos=0

    for codigo in cartelera:
        if codigo in peliculas and peliculas[codigo][1]==genero:

            total_cupos+= cartelera [codigo][1]

    print(f"El total de cupos por genero '{genero}' es: {total_cupos}")

def busqueda_precio(p_min,p_max):
    resultados=[]
    for codigo in cartelera:
        precio=cartelera[codigo][0]
        disponible=cartelera[codigo][1]
        if p_min <=precio <=p_max and disponible !=0:
            nombre=peliculas[codigo][0]
            resultados.append(nombre + "--" + codigo)
            resultados.sort()

    if len(resultados)==0:
        print("No hay peliculas en ese rango de precios.")
    else:
        print(resultados)

def actualizar_precio(codigo,nuevo_precio):
    codigo=codigo.strip().upper()
    if codigo not in cartelera:
        print("El codigo no existe.")
        return False
    cartelera[codigo][0]=nuevo_precio
    print("Precio actualizado.")
    return True

def agregar_pelicula(codigo,titulo,genero,duracion,clasificacion,idioma,es_3d,precio,cupos):
    codigo=codigo.strip().upper()

    if codigo in peliculas:
        print("El codigo ya existe.")
        return False

    if not validar_titulo(titulo):
        print("Error: Titulo inválido.")
        return False

    if not validar_genero(genero):
        print("Error: Género inválido.")
        return False
    
    if not validar_duracion_min(duracion):
        print("Error: La duración debe ser mayor a 0.")
        return False
    
    if not validar_clasificacion(clasificacion):
        print("Error: Clasificación inválida (Debe ser A, B o C).")
        return False
    
    if not validacion_idioma(idioma):
        print("Error: Idioma inválido.")
        return False

    es_3d_booleano = validacion_es_3d(es_3d)
    if es_3d_booleano is None:
        print("Error: Formato 3D inválido (Debe ser 's' o 'n').")
        return False

    if not validar_precio_positivo(precio):
        print("Error: El precio debe ser mayor a 0.")
        return False
    
    if not validar_cupos(cupos):
        print("Error: Los cupos no pueden ser negativos.")
        return False

    peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d_booleano]
    cartelera[codigo] = [precio, cupos]
    
    print("Pelicula agregada.")
    return True

def eliminar_pelicula(codigo):
    codigo = codigo.strip().upper()
    
    if codigo not in peliculas:
        print("El código no existe.")
        return False
    
    
    del peliculas[codigo]
    del cartelera[codigo]
    
    print("Pelicula eliminada.")
    return True

while True:
    mostrar_menu()
    opcion = leer_opcion()
    
    if opcion == 1:
        gen = input("Ingrese el género a consultar: ").strip().lower()
        cupos_genero(gen)
        
    elif opcion == 2:
        try:
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))
            busqueda_precio(p_min, p_max)
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
            
    elif opcion == 3:
        cod = input("Ingrese código de la película: ")
        try:
            nuevo_p = int(input("Ingrese nuevo precio: "))
            actualizar_precio(cod, nuevo_p)
        except ValueError:
            print("El precio debe ser un número entero.")
            
    elif opcion == 4:
        print("\n--- REGISTRAR NUEVA PELÍCULA ---")
        cod = input("Código (ej. P107): ")
        tit = input("Título: ")
        gen = input("Género: ").strip().lower()
        try:
            dur = int(input("Duración en minutos: "))
            clas = input("Clasificación (A/B/C): ").strip().upper()
            idi = input("Idioma: ")
            formato_3d = input("¿Es 3D? (s/n): ").strip().lower()
            pre = int(input("Precio: "))
            cup = int(input("Cupos disponibles: "))
            
           
            agregar_pelicula(cod, tit, gen, dur, clas, idi, formato_3d, pre, cup)
        except ValueError:
            print("Error: Duración, precio y cupos deben ser números enteros.")
            
    elif opcion == 5:
        cod = input("Ingrese el código de la película a eliminar: ")
        eliminar_pelicula(cod)
        
    elif opcion == 6:
        print("Programa finalizado.")
        break 