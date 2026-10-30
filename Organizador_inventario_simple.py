# Creo la lista que guardara los item.

inventario = []

print("\n--- ORGANIZADOR DE INVENTARIO ---")

# Creo el bucle que repetira el programa hasta que el usuario elija la opcion de salir.

while True:
    print("\n1. Agregar item")
    print("2. Remover item")
    print("3. Mostrar inventario")
    print("4. Verificar item")
    print("5. Salir")


    opcion = input("\nElige una opcion: ")

    # Fragmento que agrega el item ingresado por el usuario.
    if opcion == "1":
        agregar_item = input("Ingresa el item que deseas agregar: ")
        if agregar_item not in inventario:
            inventario.append(agregar_item)
            print("'",agregar_item,"'", "Ha sido agregado al inventario\n")

        else: 
            print("El item","'",agregar_item,"'","ya existe en el inventario.\n")

    # Fragmento que remueve el item ingresado por el usuario.
    elif opcion == "2":
        remove_item = input("Ingresa el nombre del ítem a remover: ")
        if remove_item not in inventario:
            print("El item'",remove_item,"'","no se encuentra en el inventario.\n")

        else:
            inventario.remove(remove_item)
            print("'",remove_item,"'","ha sido removido del inventario.\n")

    # Fragmento que muestra los item actuales.
    elif opcion == "3":
        if len (inventario)>0:
            print("\n--- Inventario Actual ---")
            for i in (inventario):
                print(f"{i}")

        else:
            print("Tu inventario esta vacio")

    # Fragmento que verifica si el item se encuentra creado.
    elif opcion == "4":
        verificar_item = input("Ingresa el nombre del item a verificar: ")
        if verificar_item not in inventario:
            print("El item",verificar_item,"no se encuentra en el inventario")

        else:
            print("El item",verificar_item,"ya existe en el inventario")

    # Fragmento que da la salida del programa.
    elif opcion == "5":
        print("Gracias por usar el organizador de inventario. ¡Hasta luego!\n")
        break

    else:
        print("La opcion que ingresaste no es valida, ingresa una opcion valida de la lista")
        