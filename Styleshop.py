#diccionarios

#diccionario descriptivo

prendas = {
'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False]
}

#diccionario operativo

bodega = {
'S001': [7990, 12],
'S002': [19990, 0],
'S003': [29990, 3],
'S004': [24990, 6],
'S005': [17990, 8],
'S006': [14990, 2]
}

#validacion diccionario descriptivo

def validar_nombre_prenda(nombre):
    if nombre.strip()!="":
        return True
    else:
        return False

def validar_Categoria(categoria):
    if categoria.strip()!="":
        return True
    else:
        return False

def validar_Talla(talla):
    if talla.strip()!="":
        return True
    else:
        return False

def validar_Color_principal(color):
    if color.strip()!="":
        return True
    else:
        return False

def validar_Material(material):
    if material.strip()!="":
        return True
    else:
        return False

def validar_prenda_unisex(es_unisex):
    opcion=es_unisex.strip().lower()
    if opcion=="s":
        return True
    elif opcion=="n":
        return False
    else:
        return None

#validacion diccionario operativo

def validar_precio_venta(precio):
    if precio >0:
        return True
    else:
        return False

def validar_unidades_bodega(unidades):
    if unidades >=0:
        return True
    else:
        return False

#funcionamiento principal :D

def unidades_categoria(categoria):
    buscar_categoria=categoria.strip().lower()
    unidades_disponibles=0

    for codigo in bodega:
        if codigo in prendas and prendas[codigo][1]==buscar_categoria:
            unidades_disponibles+=bodega[codigo][1]

    print(f"La cantidad de prendas por categoria {categoria} es de: {unidades_disponibles}")

def busqueda_precio(p_min,p_max):
    resultados=[]

    for codigo in bodega:
        precio=bodega[codigo][0]
        disponibilidad=bodega[codigo][1]
        if p_min <=precio <=p_max and disponibilidad !=0:
            nombre=prendas[codigo][0]
            resultados.append(nombre+"--"+codigo)

    resultados.sort()

    if len(resultados)==0:
        print("No hay prendas en este rango de precio.")
    else:
        print(resultados)

def actualizar_precio(codigo,nuevo_precio):
    codigo=codigo.strip().upper()

    if not codigo in bodega:
        return False
    bodega[codigo][0]=nuevo_precio
    print("Precio actualizado")
    return True

def agregar_prenda(codigo,nombre,categoria,talla,color,material,es_unisex,precio,unidades):
    codigo=codigo.strip().upper()

    if codigo in bodega:
        print("El codigo ya existe")
        return False

    if not validar_nombre_prenda(nombre):
        print("Error: El nombre de la prenda es invalido.")
        return False

    if not validar_Categoria(categoria):
        print("Error: La categoria es invalida")
        return False

    if not validar_Talla(talla):
        print("Error: La talla es invalida")
        return False

    if not validar_Color_principal(color):
        print("Error: Color invalido")
        return False

    if not validar_Material(material):
        print("Error: Material invalido")
        return False

    es_unisex_booleano=validar_prenda_unisex(es_unisex)
    if es_unisex_booleano is None:
        print("Error: Respuesta invalida(Debe ser 's' o 'n')")
        return False

    if not validar_precio_venta(precio):
        print("Error: El precio debe ser un numero entero mayor a 0")
        return False

    if not validar_unidades_bodega(unidades):
        print("Error: La cantidad de unidades disponibles debe ser mayor o igual a 0")
        return False

    prendas[codigo]=[nombre.strip().lower(),categoria.strip().lower(),talla.strip().lower(),color.strip().lower(),material.strip().lower(),es_unisex_booleano]
    bodega[codigo]=[precio,unidades]
    print("Prenda agregada")

def eliminar_prenda(codigo):
    codigo=codigo.strip().upper()

    if codigo in prendas and codigo in bodega:
        del prendas[codigo]
        del bodega[codigo]
        print("Prenda eliminada")
        return True
    else:
        print("El codigo no existe")
        return False

#menu

def mostrar_menu():
    print()
    print("=====MENU PRINCIPAL=====")
    print("1. Unidades por categoria")
    print("2. Busqueda de prendas por rango de precio")
    print("3. Actualizar precio de prenda")
    print("4. Agregar prenda")
    print("5. Eliminar prenda")
    print("6. Salir")
    print("=========================")

#leer opcion

def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opcion: "))
            if opcion >=1 and opcion <=6:
                return opcion
            else:
                print("Error: Seleccione una opcion valida")
        except ValueError:
            print("Solo se permite un numero entero positivo")

#Funcionamiento de opciones

while True:
    mostrar_menu()
    opcion=leer_opcion()

    if opcion ==1:
        categoria=input("Ingrese la categoria: ")
        unidades_categoria(categoria)

    elif opcion==2:
        try:
            p_min=int(input("Ingrese el precio minimo: "))
            p_max=int(input("Ingrese el precio maximo: "))

            if p_min>=0 and p_max >=p_min:
                busqueda_precio(p_min,p_max)

            else:
                print("Rango de precio invalido")
        except ValueError:
            print("El precio debe ser un numero entero")

    elif opcion==3:
        codigo=input("Ingrese el codigo del producto: ")
        try:
            precio=int(input("Ingrese el precio del producto: "))
            actualizar_precio(codigo,precio)
        except ValueError:
            print("Error: El precio debe ser un numero entero")

    elif opcion==4:
        print("====Registrar nuevo producto====")
        codigo=input("Ingrese el codigo del producto: ").strip().upper()

        if codigo in prendas:
            print("el codigo ya existe")
            continue

        nombre=input("Ingrese el nombre del producto: ").strip()
        categoria=input("Ingrese la categoria: ").strip()
        talla=input("Ingrese la talla: ").strip()
        color=input("Ingrese el color: ").strip()
        material=input("Ingrese el material: ").strip()

        try:
            es_unisex=input("Ingrese si la prenda es unisex: ").strip().lower()
            precio=int(input("Ingrese el precio: "))
            unidades=int(input("Ingrese la cantidad de unidades disponibles: "))

            agregar_prenda(codigo,nombre,categoria,talla,color,material,es_unisex,precio,unidades)
        except ValueError:
            print("Error: El precio y las unidades deben ser un numero entero.")

    elif opcion==5:
        codigo=input("Ingrese el codigo del producto a eliminar: ")

        eliminar_prenda(codigo)

    elif opcion==6:
        print("Programa Finalizado.")
        break

    