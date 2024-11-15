from clases import ADN, Detector, Radiacion, Sanador

if __name__ == "__main__":
    filas = 6
    columnas = 6
    adn = ADN(filas, columnas)
    adn.mostrar()

    while True:
        opcion = input("¿Qué te gustaría hacer? (1: Detectar, 2: Mutar, 3: Curar, 4: Salir): ")
        if opcion == "1":  # DETECTA
            detector = Detector()
            if not detector.detectar_mutantes(adn.matriz):
                print("No hay mutantes detectados.")
        elif opcion == "2":  # MUTA
            virus = ""
            while virus not in ["A", "T", "C", "G"]:
                virus = input("¿Con qué base quieres mutar? (A, T, C, G): ").upper()

            fila = -1
            while fila not in range(filas):
                try:
                    fila = int(input(f"¿Fila de la mutación? (0-{filas - 1}): "))
                except ValueError:
                    print("Por favor, ingresa un número válido.")

            columna = -1
            while columna not in range(columnas):
                try:
                    columna = int(input(f"¿Columna de la mutación? (0-{columnas - 1}): "))
                except ValueError:
                    print("Por favor, ingresa un número válido.")

            tipo_mutacion = ""
            while tipo_mutacion not in ["HORIZONTAL", "VERTICAL"]:
                tipo_mutacion = input("¿Tipo de mutación? (HORIZONTAL, VERTICAL): ").upper()

            mutador = Radiacion(virus)

            # Verificar espacio para la mutación
            if tipo_mutacion == "VERTICAL":
                if fila + 3 < filas:  # Verificamos si hay espacio hacia abajo
                    mutador.crear_mutante(adn.matriz, virus, (fila, columna), tipo_mutacion)  # Pasa la posición como tupla
                    print(f"Mutación vertical realizada en columna {columna} desde fila {fila}.")
                elif fila - 3 >= 0:  # Intenta mutar hacia arriba
                    mutador.crear_mutante(adn.matriz, virus, (fila - 3, columna), tipo_mutacion)  # Pasa la posición como tupla
                    print(f"Mutación vertical realizada en columna {columna} desde fila {fila - 3}.")
                else:
                    print("No hay suficiente espacio para realizar la mutación vertical.")
            elif tipo_mutacion == "HORIZONTAL":
                if columna + 3 < columnas:  # Verificamos si hay espacio hacia la derecha
                    mutador.crear_mutante(adn.matriz, virus, (fila, columna), tipo_mutacion)  # Pasa la posición como tupla
                    print(f"Mutación horizontal realizada en fila {fila} desde columna {columna}.")
                elif columna - 3 >= 0:  # Intenta mutar hacia la izquierda
                    mutador.crear_mutante(adn.matriz, virus, (fila, columna - 3), tipo_mutacion)  # Pasa la posición como tupla
                    print(f"Mutación horizontal realizada en fila {fila} desde columna {columna - 3}.")
                else:
                    print("No hay suficiente espacio para realizar la mutación horizontal.")

            adn.mostrar()
            
        elif opcion == "3":  # CURA
            sanador = Sanador()
            while sanador.sanar_mutantes(adn.matriz):  # Repetir hasta que no haya más mutantes
                adn.mostrar()
        
        elif opcion == "4":  # SALE
            break
        else:
            print("Opción no válida.")
