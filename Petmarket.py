#diccionarios

#diccionario descriptivo

productos = {
'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False]
}

#diccionario operativo

stock = {
'M001': [32990, 12],
'M002': [9990, 0],
'M003': [5490, 25],
'M004': [7990, 5],
'M005': [11990, 7],
'M006': [24990, 3]
}

#validaciones diccionario descriptivo

def validar_nombre_del_producto(nombre):
    if nombre.strip()!="":
        return True
    else:
        return False

def validar_Categoria(categoria):
    if categoria.strip()!="":
        return True
    else:
        return False

def validar_Marca(marca):
    if marca.strip()!="":
        return True
    else:
        return False

def validar_Peso_en_kilogramo(peso_kg):
    if peso_kg >0 or peso_kg >0.0:
        return True
    else:
        return False

def validar_importacion(es_importado):
    opcion=es_importado.strip().lower()
    if opcion == "s":
        return True
    elif opcion == "n":
        return False
    else:
        return None

def validar_orientado_a_cachorros(es_para_cachorro):
    opcion=es_para_cachorro.strip().lower()
    if opcion == "s":
        return True
    elif opcion =="n":
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

#Funcionamiento principal 

def unidades_categoria(categoria):
    buscar_categoria=categoria.strip().lower()
    unidades_disponibles=0

    for codigo in stock:
        if codigo in productos and productos[codigo][1].lower()==buscar_categoria:
            unidades_disponibles+=stock[codigo][1]

    print(f"El total de unidades por categoria '{categoria}' es de : {unidades_disponibles}")

def busqueda_precio(p_min,p_max):
    resultados=[]

    for codigo in stock:
        precio=stock[codigo][0]
        disponibilidad=stock[codigo][1]

        if p_min <=precio <=p_max and disponibilidad !=0:
            nombre=productos[codigo][0]
            resultados.append(nombre+"--"+codigo)

    resultados.sort()

    if len(resultados)==0:
        print("No hay productos en ese rango de precios.")
    else:
        print(resultados)

def actualizar_precio(codigo,nuevo_precio):
    codigo=codigo.strip().upper()

    if not codigo in stock:
        return False
    
    stock[codigo][0]=nuevo_precio
    print("Precio actualizado")
    return True

def agregar_producto(codigo,nombre,categoria,marca,peso_kg,es_importado,es_para_cachorros,precio,unidades):

    if codigo in stock:
        print("El codigo ya existe")
        return False

    if not validar_nombre_del_producto(nombre):
        print("Error: Nombre del producto invalido")
        return False

    if not validar_Categoria(categoria):
        print("Error: Nombre de categoria invalido")
        return False

    if not validar_Marca(marca):
        print("Error: Nombre de marca invalido")
        return False

    if not validar_Peso_en_kilogramo(peso_kg):
        print("Error: El peso debe ser mayor a 0")
        return False

    es_importado_booleano=validar_importacion(es_importado)
    if es_importado_booleano is None:
        print("Error: Respuesta de importacion invalida(Debe ser 's' o 'n' )")
        return False

    es_para_cachorros_booleano=validar_orientado_a_cachorros(es_para_cachorros)
    if es_para_cachorros_booleano is None:
        print("Error: Respuesta Invalida(Debe ser 's' o 'n')")
        return False

    if not validar_precio_venta(precio):
        print("Error: El precio de venta debe ser mayor a 0")
        return False

    if not validar_unidades_bodega(unidades):
        print("Error: La cantidad de unidades debe ser igual o mayor a 0")
        return False

    productos[codigo]=[nombre.strip().lower(),categoria.strip().lower(),marca.strip().lower(),peso_kg,es_importado_booleano,es_para_cachorros_booleano]
    stock[codigo]=[precio,unidades]
    print("Producto agregado correctamente.")

def eliminar_producto(codigo):
    codigo=codigo.strip().upper()

    if codigo in productos and codigo in stock:
        del productos[codigo]
        del stock[codigo]
        print("Producto eliminado correctamente")
        return True
    else:
        print("El codigo no existe")
        return False

#menu

def mostrar_menu():
    print()
    print("=====MENU PRINCIPAL=====")
    print("1. Unidades por categoria")
    print("2. Busqueda de producto por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")

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

while True:
    mostrar_menu()
    opcion=leer_opcion()

    if opcion==1:
        categoria=input("Ingrese el nombre de la categoria: ")
        unidades_categoria(categoria)

    elif opcion==2:
        try:
            p_min=int(input("Ingrese el precio minimo: "))
            p_max=int(input("Ingrese el precio maximo: "))

            if p_min >=0 and p_max >=p_min:
                busqueda_precio(p_min,p_max)
            else:
                print("Error: Rango de precios invalido")
        except ValueError:
            print("El precio debe ser un numero entero.")

    elif opcion==3:
        codigo=input("Ingrese el codigo de su producto: ")
        try:
            precio=int(input("Ingrese el nuevo precio: "))
            actualizar_precio(codigo,precio)
        except ValueError:
            print("Error: El nuevo precio del producto debe ser un numero entero")

    elif opcion==4:
        print("====Registrar nuevo producto====")

        codigo=input("Ingrese el codigo del producto: ").strip().upper()

        if codigo in productos:
            print("El codigo ya existe")
            continue

        nombre=input("Ingrese el nombre del producto: ").strip()
        categoria=input("Ingrese la categoria: ").strip()
        marca=input("Ingrese la marca: ").strip()

        try:
            peso_kg=float(input("Ingrese el peso del producto: "))
            es_importado=input("Ingrese si el producto es importado: ").strip().lower()
            es_para_cachorros=input("Ingrese si el producto es para cachorro: ").strip().lower()
            precio=int(input("Ingrese el nuevo precio del producto: "))
            unidades=int(input("Ingrese la cantidad de unidades disponibles: "))

            agregar_producto(codigo,nombre,categoria,marca,peso_kg,es_importado,es_para_cachorros,precio,unidades)
        except ValueError:
            print("Error el precio,las unidades deben ser un numero entero.")

    elif opcion==5:
        codigo=input("Ingrese el codigo del producto a eliminar: ")

        eliminar_producto(codigo)

    elif opcion==6:
        print("Programa finalizado.")
        break