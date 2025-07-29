def sala():
    boletos = 0
    total = 0
    sala = []
    funciones = ["Spider-Man", "Avatar", "Mario Bros", "Oppenheimer"]

    def mostrar_funciones():
        print("Funciones disponibles")
        for clave, valor in enumerate(funciones, 1):
            print(f"{clave}. {valor}")

    def agregar_cliente(nombre, **datos):
        cliente = {"nombre": nombre}
        cliente.update(datos)
        sala.append(cliente)
        print("\n---Resumen---")
        for clave, valor in cliente.items():
            print(f"{clave.capitalize()}: {valor}")

    def comprar_boletos():
        nonlocal boletos, total
        boleto = int(input("Ingrese el número de boletos que desea comprar: "))
        if boleto > 0:
            boletos += boleto
            total += boleto * 40
            print(f"Total acumulado: Q{total}")
            return boleto
        else:
            print("Ingrese un numero valido")
            return 0

    while True:
        print("\n--- Menu ---")
        print("1. Ingresar cliente\n.2. Mostrar clientes registrados.\n3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            mostrar_funciones()
            seleccion = int(input("Seleccione el numero de la pelicula: "))
            if 1 <= seleccion <= len(funciones):
                pelicula = funciones[seleccion - 1]
                cantidad_boletos = comprar_boletos()
                if cantidad_boletos > 0:
                    agregar_cliente(nombre, pelicula=pelicula, boletos=cantidad_boletos, total=cantidad_boletos*40)
            else:
                print("Seleccione una de las opciones.")
        elif opcion == "2":
            print("Lista de clientes")
            for cliente in sala:
                print(cliente)
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

sala()
