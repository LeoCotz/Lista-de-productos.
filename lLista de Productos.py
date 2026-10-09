productos = [] 


def pedir_texto(mensaje):
    """Pide un texto y repite la consulta hasta que no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error: el dato no puede estar vacío.")
        else:
            return texto


def pedir_precio(mensaje):
    """Pide un precio entero positivo (sin centavos)."""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Error: el precio no puede estar vacío.")
        elif not valor.isdigit():
            print("Error: ingresá solo números enteros, sin centavos ni símbolos.")
        elif int(valor) <= 0:
            print("Error: el precio debe ser mayor a 0.")
        else:
            return int(valor)


def agregar_producto():
    print("\n--- Agregar producto ---")
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_texto("Categoría: ")
    precio = pedir_precio("Precio (sin centavos): ")

    productos.append([nombre, categoria, precio])
    print(f"Producto '{nombre}' agregado correctamente.")


def mostrar_productos():
    print("\n--- Productos registrados ---")
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        for i in range(len(productos)):
            nombre = productos[i][0]
            categoria = productos[i][1]
            precio = productos[i][2]
            print(f"{i + 1}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")


def buscar_producto():
    print("\n--- Buscar producto ---")
    if len(productos) == 0:
        print("No hay productos registrados para buscar.")
        return

    busqueda = pedir_texto("Ingresá el nombre a buscar: ").lower()
    encontrados = 0

    for i in range(len(productos)):
        if busqueda in productos[i][0].lower():
            if encontrados == 0:
                print("\nResultados encontrados:")
            print(f"{i + 1}. Nombre: {productos[i][0]} | "
                  f"Categoría: {productos[i][1]} | Precio: ${productos[i][2]}")
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron resultados.")


def eliminar_producto():
    print("\n--- Eliminar producto ---")
    if len(productos) == 0:
        print("No hay productos para eliminar.")
        return

    mostrar_productos()

    while True:
        entrada = input("\nIngresá el número del producto a eliminar: ").strip()
        if entrada == "":
            print("Error: no puede estar vacío.")
        elif not entrada.isdigit():
            print("Error: ingresá un número válido.")
        else:
            posicion = int(entrada)
            if posicion < 1 or posicion > len(productos):
                print(f"Error: el número debe estar entre 1 y {len(productos)}.")
            else:
                eliminado = productos.pop(posicion - 1)
                print(f"Producto '{eliminado[0]}' eliminado correctamente.")
                break


def mostrar_menu():
    print("\nSistema de gestión básica de productos")
    print()
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")


def main():
    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("\nElegí una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("\nSaliendo del sistema. ¡Hasta luego!")
        else:
            print("Opción inválida. Elegí un número del 1 al 5.")


main()