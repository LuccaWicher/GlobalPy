# **Detector y Mutador de ADN**

Este programa analiza secuencias de ADN representadas en una matriz de 6x6 para detectar mutaciones y permite modificarlas (mutarlas) o sanarlas. Se centra en las bases nitrogenadas del ADN: **Adenina (A)**, **Timina (T)**, **Citosina (C)** y **Guanina (G)**.

---

## **Descripción**

Una secuencia de ADN se considera mutante si contiene al menos 4 bases nitrogenadas iguales seguidas en alguna de las siguientes direcciones:
- **Horizontal**
- **Vertical**
- **Diagonal**

El programa incluye clases que permiten:
- **Detectar mutantes** en una matriz de ADN.
- **Crear mutantes** de manera horizontal, vertical o diagonal.
- **Sanar ADN**, generando nuevas secuencias sin mutaciones.

### **Ejemplo de Matriz de ADN**
Una matriz de ADN se representa como una lista de strings:
```python
matriz = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]


## **Flujo del Programa**
Solicita al usuario una matriz de ADN. Esta no importa si esta escrita en mayusculas o minisculas ya que se tomara todo como mayusculas
Pregunta si desea:
Detectar mutaciones. (1)
Mutar. (2) 
Sanar el ADN. (3)
Salir (4)
Según la opción seleccionada:
Se utiliza la clase Detector para verificar mutaciones.
Se instancian las clases Radiación o Virus para mutar el ADN.
Se utiliza la clase Sanador para crear un nuevo ADN sin mutaciones.
Muestra la matriz final y un mensaje con el resultado.

## **Ejemplo de Entrada y Salida**
Introduce la fila 1 del ADN (longitud 6 y solo A, T, C o G): AGATCA
Introduce la fila 2 del ADN (longitud 6 y solo A, T, C o G): GATTCA
Introduce la fila 3 del ADN (longitud 6 y solo A, T, C o G): CAACAT
Introduce la fila 4 del ADN (longitud 6 y solo A, T, C o G):GAGCTA
Introduce la fila 5 del ADN (longitud 6 y solo A, T, C o G):ATTGCG
Introduce la fila 6 del ADN (longitud 6 y solo A, T, C o G):CTGTTC

¿Qué te gustaría hacer? (1: Detectar, 2: Mutar, 3: Curar, 4: Salir):

Salida
Si se detecta una mutación (1):
¡Mutante horizontal detectado en la fila 3 columna 3! Base: C

Si se realiza una mutación (2):
En esta opcion, tendras libertar para elegir la base con la cual mutar, la columna y la fila en la quee realizara la misma, tambien teniendo libertad para elegir si hacerla vertical u horizontal
suponiendo que la ingresaste base T, fila 0, columna 0 y hacerla de manea horizontal, el output seria 
Mutación horizontal realizada en columna 0 desde fila 0. 
TTTTCA
GATTCA
CAACAT
GAGCTA
ATTGCG
CTGTTC

Si se realiza la sanar (3):
¡Mutante vertical detectado en la columna 2 fila 3! Base: T. Este mensaje nos lo muestra porque en el intento de sanar, se encontro un nuevo mutante, no debemos preocuparnos por eso ya que sera un bucle infinito hasta que no se detecte ningun tipo de mutante, y se nos entrega el ADN sano
¡Matriz curada!
T G A A A C
G A T G G A
C A A C C C
C G T C G C
G T G C C T
T G G A A A

Si se realiza Salir (4):
Se nos mostrara un mensajeopr pantalla y se nos mostrara como quedo nuestro ADN

En lugar de elegir cualquier tipo de caracter, el cual no sea, "A", "C", "T" o "G" El programa nos pondra un mensaje de error, y terminara el programa