import random

class ADN:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = self.crear_matriz()

    def crear_matriz(self):
        matriz = []
        for i in range(self.filas):
            while True:
                fila_adn = input(f"Introduce la fila {i + 1} del ADN (longitud {self.columnas} y solo A, T, C o G): ")
                fila_adn = fila_adn.upper()
                if len(fila_adn) == self.columnas and all(base in "ATCG" for base in fila_adn):
                    matriz.append(list(fila_adn))
                    break
                else:
                    print("Entrada inválida. Asegúrate de que la longitud sea correcta y solo contenga A, T, C o G.")
        return matriz

    def mostrar(self):
        for fila in self.matriz:
            print(' '.join(fila))


class Detector:
    def __init__(self):
        pass  # No necesitamos un atributo "matriz", ya que la matriz se pasa como argumento a los métodos

    def detectar_mutantes(self, matriz):
        if self.detectar_horizontal(matriz) or self.detectar_vertical(matriz) or self.detectar_diagonal(matriz):
            return True
        return False

    def detectar_vertical(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0]) if filas > 0 else 0
        for j in range(columnas):
            contador = 0
            for i in range(filas):
                if i == 0 or matriz[i][j] == matriz[i - 1][j]:
                    contador += 1
                else:
                    contador = 1
                if contador >= 4:
                    print(f"¡Mutante vertical detectado en la columna {j} fila {i}! Base: {matriz[i][j]}")
                    return True
        return False

    def detectar_horizontal(self, matriz):
        for i in range(len(matriz)):
            contador = 0
            for j in range(len(matriz[i])):
                if j == 0 or matriz[i][j] == matriz[i][j - 1]:
                    contador += 1
                else:
                    contador = 1
                if contador >= 4:
                    print(f"¡Mutante horizontal detectado en la fila {i} columna {j}! Base: {matriz[i][j]}")
                    return True
        return False

    def detectar_diagonal(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0]) if filas > 0 else 0

        # Revisamos diagonales de izquierda a derecha
        for i in range(filas):
            for j in range(columnas):
                if i + 3 < filas and j + 3 < columnas:
                    if (matriz[i][j] == matriz[i + 1][j + 1] == 
                        matriz[i + 2][j + 2] == matriz[i + 3][j + 3]):
                        print(f"¡Mutante diagonal (izquierda a derecha) detectado comenzando en fila {i}, columna {j}! Base: {matriz[i][j]}")
                        return True

        # Revisamos diagonales de derecha a izquierda
        for i in range(filas):
            for j in range(columnas):
                if i + 3 < filas and j - 3 >= 0:
                    if (matriz[i][j] == matriz[i + 1][j - 1] == 
                        matriz[i + 2][j - 2] == matriz[i + 3][j - 3]):
                        print(f"¡Mutante diagonal (derecha a izquierda) detectado comenzando en fila {i}, columna {j}! Base: {matriz[i][j]}")
                        return True
        return False


class Mutador:
    def __init__(self, base_nitrogenada):
        self.base_nitrogenada = base_nitrogenada

    def crear_mutante(self, matriz, posicion_inicial, orientacion):
        pass  # Método vacío para ser implementado en clases hijas


class Radiacion(Mutador):
    def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        fila, columna = posicion_inicial

        # Verificación de mutación vertical
        if orientacion_de_la_mutacion == "VERTICAL":
            if fila + 3 < len(matriz):  # Verificamos que haya espacio suficiente hacia abajo
                for i in range(4):
                    matriz[fila + i][columna] = base_nitrogenada
            else:
                print(f"No hay espacio suficiente para mutar verticalmente desde ({fila}, {columna}).")

        # Verificación de mutación horizontal
        elif orientacion_de_la_mutacion == "HORIZONTAL":
            if columna + 3 < len(matriz[0]):  # Verificamos que haya espacio suficiente hacia la derecha
                for i in range(4):
                    matriz[fila][columna + i] = base_nitrogenada
            else:
                print(f"No hay espacio suficiente para mutar horizontalmente desde ({fila}, {columna}).")

        else:
            print(f"Tipo de mutación no reconocido: {orientacion_de_la_mutacion}")
        
        return matriz  # Retornamos la matriz modificada


class Virus(Mutador):
    def crear_mutante(self, matriz, base_nitrogenada, posicion_inicial):
        fila, columna = posicion_inicial
        # Mutación diagonal
        for i in range(4):
            if fila + i < len(matriz) and columna + i < len(matriz[0]):
                matriz[fila + i][columna + i] = base_nitrogenada
        return matriz  # Retornamos la matriz mutada

class Sanador:
    def __init__(self):
        self.bases = ['A', 'T', 'C', 'G']

    def sanar_mutantes(self, matriz):
        detector = Detector()
        if detector.detectar_mutantes(matriz):
            for i in range(len(matriz)):
                for j in range(len(matriz[0])):
                    matriz[i][j] = random.choice(self.bases)  # Generamos una nueva matriz de ADN con bases aleatorias
            print("¡Matriz curada!")
            return True  # Retorna True si habia mutantes
        else:
            print("No hay mutantes para curar.")
            return False  # Retorna False si no había mutantes

    def mostrar_matriz(self, matriz):
        for fila in matriz:
            print(' '.join(fila))  # Imprime la matriz de forma legible 6x6

