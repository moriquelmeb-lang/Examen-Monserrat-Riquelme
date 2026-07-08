##### FUNCIONES ##########
def leerMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")

    while True:
        try:
            opcion = int(input("Ingrese una opción del menú: "))
            if opcion>0 and opcion<=6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def stock_plataforma(plataforma,diccionarioJuegos,diccionarioInventario):
    plataforma = plataforma.strip().upper()
    acumulador = 0
    for claveJuegos,valorJuegos in diccionarioJuegos.items():
        if valorJuegos[1] == plataforma:
            for claveInventario,valorInventario in diccionarioInventario.items():
                if claveJuegos == claveInventario:
                    acumulador += valorInventario[1]
    
    print(f"La plataforma {plataforma} cuenta con un stock total de {acumulador}")

def busqueda_precio(p_min, p_max,diccionarioJuegos,diccionarioInventario):
    lista = []
    for claveInventario,valorInventario in diccionarioInventario.items():
        if valorInventario[0]>=p_min and valorInventario[0]<=p_max and valorInventario[1]>0:
            for claveJuegos,valorJuegos in diccionarioJuegos.items():
                if claveInventario == claveJuegos:
                    lista.append(f"{valorJuegos[0]}--{claveJuegos}")
                    break
    
    if len(lista) == 0:
        print("No hay juegos en ese rango de precios.")
    else:
        lista.sort()
        for juegos in lista:
            print(juegos)

def actualizar_precio(codigo, nuevo_precio,diccionarioInventario):
    for claveInventario in diccionarioInventario.keys():
        if codigo == claveInventario:
            diccionarioInventario[codigo][0] = nuevo_precio
            return True
    
    return False

def eliminar_juego(codigo,diccionarioInventario,diccionarioJuegos):
    for claveInventario in diccionarioInventario.keys():
        if codigo == claveInventario:
            del diccionarioInventario[codigo]
            del diccionarioJuegos[codigo]
            return True
        else:
            return False

###### VALIDADCIONES OPCION 4 ##########
def validarCodigo(codigo):
    codigo = codigo.strip().upper()
    if codigo == "":
        return False
    else:
        return True

def validarTitulo(titulo):
    titulo = titulo.strip()
    if titulo == "":
        return False
    else:
        return True

def validarPlataforma(plataforma):
    plataforma = plataforma.strip()
    if plataforma == "":
        return False
    else:
        return True

def validarGenero(genero):
    genero = genero.strip()
    if genero == "":
        return False
    else:
        return True

def validarClasificacion(clasificacion):
    clasificacion = clasificacion.upper()
    if clasificacion == 'E' or clasificacion == 'T' or clasificacion == 'M':
        return True
    else:
        return False

def validarMultiplayer(multiplayer):
    multiplayer = multiplayer.lower()
    if multiplayer == 's' or multiplayer == 'n':
        return True
    else:
        return False

def validarEditor(editor):
    editor = editor.strip()
    if editor == "":
        return False
    else:
        return True

def validarPrecio(precio):
    precio = int(precio)
    if precio>0:
        return True
    else:
        return False

def validarStock(stock):
    stock = int(stock)
    if stock>=0:
        return True
    else:
        return False

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock,diccionarioInventario,diccionarioJuegos):
    for claveInventario in diccionarioInventario.keys():
        if claveInventario != codigo:
            listaJuegos = [titulo, plataforma, genero, clasificacion, multiplayer, editor]
            listaInventario = [precio, stock]

            diccionarioJuegos[codigo] = listaJuegos
            diccionarioInventario[codigo] = listaInventario
            return True
        else:
            return False


########### PROGRAMA PRINCIPAL ###########
juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}

inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}   

while True:
    opcionSeleccionada = leerMenu()

    if opcionSeleccionada == 1:
        plataformaPorBuscar = input("Ingrese la plataforma que desea buscar: ")
        stock_plataforma(plataformaPorBuscar,juegos,inventario)

    elif opcionSeleccionada == 2:
        while True:
            try:
                precioMinimo = int(input("Ingrese el precio mínimo a asignar: "))
                precioMaximo = int(input("Ingrese el precio máximo a asignar: "))
                if precioMinimo<0 or precioMinimo>precioMaximo:
                    print("Debe ingresar valores enteros")
                else:
                    busqueda_precio(precioMinimo,precioMaximo,juegos,inventario)
                    break
            except ValueError:
                print("Debe ingresar valores enteros")
    elif opcionSeleccionada == 3:
        while True:
            codigoPorBuscar = input("Ingrese código para nueva asignación de precio: ").strip().upper()
            while True:
                try:
                    nuevoPrecio = int(input("Ingrese el nuevo precio a asignar: "))
                    if nuevoPrecio<0:
                        print("Ingrese un número entero positivo")
                    else:
                        break
                except ValueError:
                    print("Ingrese un número entero positivo")
            
            actualizado = actualizar_precio(codigoPorBuscar,nuevoPrecio,inventario)
            if actualizado == True:
                print("Precio actualizado")
            else:
                print("El código no existe")
            
            otroPrecio = input("¿Desea actualizar otro precio (s/n)?: ").lower()
            if otroPrecio == 's':
                continue
            else:
                break

    elif opcionSeleccionada == 4:
        codigoAgregar = input("Ingrese código a agregar: ")
        tituloAgregar = input("Ingrese título a agregar: ")
        plataformaAgregar = input("Ingrese plataforma a agregar: ")
        generoAgregar = input("Ingrese género a agregar: ")
        clasificacionAgregar = input("Ingrese clasificación a agregar (E/T/M): ")
        multiplayerAgregar = input("Ingrese multiplayer a agregar (s/n): ")
        editorAgregar = input("Ingrese editor a agregar: ")
        precioAgregar = int(input("Ingrese precio a agregar: "))
        stockAgregar = int(input("Ingrese stock a agregar: "))

        codigoValidado = validarCodigo(codigoAgregar)
        tituloValidado = validarTitulo(tituloAgregar)
        plataformaValidado = validarPlataforma(plataformaAgregar)
        generoValidado = validarGenero(generoAgregar)
        clasificacionValidado = validarClasificacion(clasificacionAgregar)
        multiplayerValidado = validarMultiplayer(multiplayerAgregar)
        editorValidado = validarEditor(editorAgregar)
        precioValidado = validarPrecio(precioAgregar)
        stockValidado = validarStock(stockAgregar)

        if codigoValidado == True and tituloValidado == True and plataformaValidado == True and generoValidado == True and clasificacionValidado == True and multiplayerValidado == True and editorValidado == True and precioValidado == True and stockValidado == True:
            agregarCorrectamente = agregar_juego(codigoAgregar,tituloAgregar,plataformaAgregar,generoAgregar,clasificacionAgregar,multiplayerAgregar,editorAgregar,precioAgregar,stockAgregar,inventario,juegos)
            if agregarCorrectamente == True:
                print( "Juego agregado")
            else:
                print("El código ya existe" )


    elif opcionSeleccionada == 5:
        codigoPorEliminar = input("Ingrese código del juego que desea eliminar: ").strip().upper()
        eliminar = eliminar_juego(codigoPorEliminar,inventario,juegos)
        if eliminar == True:
            print("Juego eliminado")
        else:
            print("El código no existe")
    elif opcionSeleccionada == 6:
        print("Programa finalizado.")
        break