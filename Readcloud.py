#diccionarios

#diccionario descriptivo
libros = {
'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
'L002': ['Python en Ruta', 'M. Diaz', 'tecnologia', 2023, 'CodeBooks', True],
'L003': ['Mar y Viento', 'C. Silva', 'poesia', 2017, 'Litoral', False],
'L004': ['Historia Breve', 'J. Perez', 'historia', 2015, 'Cronos', False],
'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficcion', 2021, 'Orion', True],
'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False]
}

#diccionario operativo
prestamos = {
'L001': [500, 4],
'L002': [700, 0],
'L003': [300, 10],
'L004': [400, 2],
'L005': [600, 1],
'L006': [350, 6]
}

#validaciones diccionario descriptivo

def validar_titulo_del_libro(titulo):
    if titulo.strip()!="":
        return True
    else:
        return False

def validar_nombre_del_autor(autor):
    if autor.strip()!="":
        return True
    else:
        return False

def validar_genero_literario(genero):
    if genero.strip()!="":
        return True
    else:
        return False

def validar_anio_de_publicacion(anio):
    if anio >0:
        return True
    else:
        return False
    
def validar_Editorial(editorial):
    if editorial.strip()!="":
        return True
    else:
        return False

def validar_novedad_editorial(es_novedad):
    opcion=es_novedad.strip().lower()
    if opcion=="s":
        return True
    elif opcion=="n":
        return False
    else:
        return None

#validaciones diccionario operativo

def validar_multa_por_atraso(precio_multa):
    if precio_multa >0:
        return True
    else:
        return False

def validar_copias(copias_disponibles):
    if copias_disponibles >=0:
        return True
    else:
        return False

#funcionamiento principal sisi

def copias_genero(genero):
    copias_buscar=genero.strip().lower()
    total_copias=0

    for codigo in prestamos:
        if codigo in libros and libros[codigo][2]==copias_buscar:
            total_copias+=prestamos[codigo][1]

    print(f"El total de copias por genero '{genero}' es de :{total_copias}")

def busqueda_multa(p_min,p_max):
    resultados=[]

    for codigo in prestamos:
        precio=prestamos[codigo][0]
        disponible=prestamos[codigo][1]

        if p_min <=precio <=p_max and disponible !=0:
            nombre=libros[codigo][0]
            resultados.append(nombre+"--"+codigo)

    resultados.sort

    if len(resultados)==0:
        print("No hay libros en ese rango de multa.")
    else:
        print(resultados)

def actualizar_multa(codigo,nueva_multa):
    codigo=codigo.strip().upper()
    if not codigo in prestamos:
        return False
    prestamos[codigo][0]=nueva_multa
    return True

def agregar_libro(codigo,titulo,autor,genero,anio,editorial,es_novedad,precio_multa,copias_disponibles):
    if codigo in prestamos:
        print("El codigo ya existe")
        return False

    if not validar_titulo_del_libro(titulo):
        print("Error: El titulo del libro es inválido")
        return False

    if not validar_nombre_del_autor(autor):
        print("Error: El nombre del autor es inválido")
        return False

    if not validar_genero_literario(genero):
        print("Error: El genero que busca es invalido")
        return False

    if not validar_anio_de_publicacion(anio):
        print("Error: El año debe ser mayor a 0")
        return False

    if not validar_Editorial(editorial):
        print("Error: El nombre de la editorial es invalido")
        return False

    es_novedad_booleano=validar_novedad_editorial(es_novedad)
    if es_novedad_booleano is None:
        print("Error: Es novedad invalida (Debe ser 's' o 'n' ) ")
        return False

    if not validar_multa_por_atraso(precio_multa):
        print("Error: El precio de la multa debe ser mayor a 0")
        return False

    if not validar_copias(copias_disponibles):
        print("Error: Las copias disponibles deben ser igual o mayor a 0")
        return False

    libros[codigo]=[titulo.strip().lower(),autor.strip().lower(),genero.strip().lower(),anio,es_novedad_booleano]
    prestamos[codigo]=[precio_multa,copias_disponibles]
    print("Recorrido agregado correctamente")

def eliminar_libro(codigo):
    codigo=codigo.strip().upper()
    if codigo in libros and codigo in prestamos:
        del libros[codigo]
        del prestamos[codigo]
        print("Plan eliminado correctamente")
        return True
    else:
        print("El codigo no existe")
        return False

#El menu y leer las opciones
def mostrar_menu():
    print()
    print("=====MENU PRINCIPAL======")
    print("1. Copias por genero")
    print("2. Busqueda de libros por rango de multa")
    print("3. Actualizar multa de libro")
    print("4. Agregar libro")
    print("5. Eliminar libro")
    print("6. Salir")
    print("=============================")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opción: "))
            if opcion >=1 and opcion <=6:
                return opcion
            else:
                print("Error: Seleccione una opcion valida")
        except ValueError:
            print("Solo se permite un numero entero positivo.")

#Funcionamiento del menu

while True:
    mostrar_menu()
    opcion=leer_opcion()

    if opcion==1:
        genero=input("Ingrese el genero de su libro.")
        copias_genero(genero)           

    elif opcion==2:
        try:
            p_min=int(input("Ingrese el precio minimo: "))
            p_max=int(input("ingrese el precio maximo: "))

            if p_min >=0 and p_max >=p_min:
                busqueda_multa(p_min,p_max)
            else:
                print("Error: Rango de precios invalidos.")
        except ValueError:
            print("Error: El precio debe ser un numero entero")

    elif opcion==3:
        codigo=input("Ingrese el codigo(ej. P202): ").strip().upper()
        try:
            nueva_multa=int(input("Ingrese la nueva multa: "))
            actualizar_multa(codigo,nueva_multa)
        except ValueError:
            print("Error: La nueva multa debe ser un numero entero")

    elif opcion==4:
        print("====REGISTRAR NUEVO LIBRO=====")
        codigo=input("Ingrese el codigo").strip().upper()
        if codigo in libros:
            print("El codigo ya existe")
            continue

        titulo=input("Ingrese el titulo del libro:").strip()
        autor=input("Ingrese el nombre del autor: ").strip()
        genero=input("Ingrese el genero del libro:").strip()

        try:
            anio=int(input("Ingrese el año de publicacion del libro: "))
            editorial=input("Ingrese el nombre de la editorial: ")
            novedad_input=input("¿Es novedad? (s/n)").strip().lower()
            precio_multa=int(input("Ingrese el nuevo precio de la multa: "))
            copias_disponibles=int(input("Ingrese la cantidad de copias disponibles: "))

            agregar_libro(codigo,titulo,autor,genero,anio,editorial,novedad_input,precio_multa,copias_disponibles)
        except ValueError:
            print("Error: Precio de la multa,año y copias deben ser un numero entero")

    elif opcion==5:
        codigo=input("Ingrese el codigo del libro que desea eliminar: ")
        eliminar_libro(codigo)

    elif opcion== 6:
        print("Programa finalizado.")
        break