# 31/10/2020
# Angel Rodríguez

# 1. Escriba un programa para imprimir el texto suministrado en el formato mostrado:
# Texto: “Twinkle, twinkle, listtle start, How I wonder what you are! Up above the world so
# high, Like a diamond in the sky. Twinkle, twinkle, listtle start, How I wonder what you are”
# Formato:
#
#       Twinkle, twinkle, listtle start,
#             How I wonder what you are!
#                   Up above the world so high,
#                   Like a diamond in the sky.
#             Twinkle, twinkle, listtle start,
#       How I wonder what you are

def ejercicio1():
    print("\tTwinkle, twinkle, listtle start,")
    print("\t\tHow I wonder what you are!")
    print("\t\t\tUp above the world so high,")
    print("\t\t\tLike a diamond in the sky.")
    print("\t\tTwinkle, twinkle, listtle start,")
    print("\tHow I wonder what you are")

# 2. Escriba un programa que dado un número n (0 < n ≤ 40), imprima por la pantalla una
# escalera de altura n y base n, usando símbolos “#”. Por ejemplo: entrada n = 4, salida
# (observe que la escalera va de izquierda a derecha):
#       #
#      ##
#     ###
#    ####

def ejercicio2(n=4):
    try:
        nAsNumber = int(n)
    except:
        print("Eso no parece ser un numero. Ejecute el programa de nuevo.")
        return
    if (nAsNumber > 40 or nAsNumber <= 0):
        print('Introduzca un valor entre 0 y 40')
        return
    for i in range(nAsNumber):
        print(' ' * (nAsNumber-i-1) + '#' * (i+1))

# 3. Escriba un programa que acepte el radio de un círculo por el usuario y calcule y muestre
# por pantalla el área. (La fórmula es Á𝑟𝑒𝑎 = 𝜋𝑟^2, donde r es el radio del círculo) Ayuda: en
# el módulo math puede encontrar el valor de 𝜋.

from math import pi

def ejercicio3():
    entrada = input("Ingrese el radio del circulo: ")
    try:
        r = float(entrada)
    except:
        print("Eso no parece ser un numero. Ejecute el programa de nuevo.")
        return
    area = pi * r ** 2
    print(f"El area del circulo de radio {r} es: {area}")
    return area

# 4. Escriba un programa que calcule el volumen de esfera de un radio r dado

from math import pi

def ejercicio4():
    entrada = input("Ingrese el radio de la esfera: ")
    try:
        r = float(entrada)
    except:
        print("Eso no parece ser un numero. Ejecute el programa de nuevo.")
        return
    vol = pi * r**3 * 4/3
    print(f"El volumen de la esfera de radio {r} es de: {vol}")

# 5. Escriba un programa que solicite el nombre y el apellido (separadamente) y luego
# imprímalos en orden inverso

def ejercicio5():
    name = input("ingrese su nombre: ")
    lastname = input("ingrese su apellido: ")
    full = f"{name} {lastname}"
    print(f"{full} alrevez es: {full[::-1]}")

# 6. Escriba un programa que acepte una secuencia de números separados por coma y genere
# un list y un tuple de strings con esos números.
# Por ejemplo: Secuencia de entrada: “3,5,7,23”
# Salida: List: [´3´, ´5´, ´7´, ´23´] Tuple: (´3´, ´5´, ´7´, ´23´)

def ejercicio6():
    sequence = input("Introduzca una secuencia de numeros separados por comas: ")
    sequenceAsList = sequence.split(',')
    sequenceAsTuple = tuple(sequenceAsList)
    print(f"List: {sequenceAsList}\nTuple: {sequenceAsTuple}")
    return [sequenceAsList, sequenceAsTuple]

# 7. Escriba un programa que acepte el nombre de un archivo desde la entrada e imprima la
# extensión de ese archivo. Ejemplo: ingresa abc.java, salida: java

import os

def ejercicio7(filename = 'abc.java'):
    fileExtension = os.path.splitext(filename)[1]
    return fileExtension[1:]

# 8. Escriba un programa que reciba un número entero (positivo o negativo) y por la salida lo
# muestre de forma inversa. Ejemplo, entrada: -123, salida: -321

def ejercicio8(numAsStr: str = "-123"):
    try:
        num = int(numAsStr)
    except:
        print("Eso no parece ser un numero. Ejecute el programa de nuevo.")
    inputIsNegative = num < 0
    sectionToReverse = str(numAsStr)[1:] if inputIsNegative else str(numAsStr)
    reversedNumber = sectionToReverse[::-1]
    return int(f"-{reversedNumber}") if inputIsNegative else int(reversedNumber)

# 9. Si la suma de todos los números naturales por debajo de 10 que son múltiplos de 3 o 5,
# tenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23. Encuentre la suma de los múltiplos
# de 3 y 5 por debajo de 1000

def ejercicio9():
    return "TODO"

# 10. La serie de Fibonacci es aquella que se genera como la suma de los dos números anteriores.
# Por ejemplo, la serie para los números menores a 100 sería:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# Escriba un programa que acepte de un usuario un número entero, e indique por la salida los
# números de la serie de Fibonacci menores al número ingresado.

def ejercicio10():
    numAsStr = input(
        "Introduzca el número al cual le desee calcular la secuencia de fibonacci: ")
    try:
        num = int(numAsStr)
    except:
        print("Eso no parece ser un numero. Ejecute el programa de nuevo.")

    def fibo(n: int = 0):
        if n <= 0:
            print("La serie de fibonacci no puede ser calculada para número negativos")
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibo(n-1) + fibo(n-2)

    print(f"La serie fibonacci hasta el numero {num} es de: {fibo(num)}")

# 11. Tomando como ejemplo el ejercicio 7. Encuentre la suma de los números pares de una serie
# de Fibonacci menores o iguales a 4.000.000.

def ejercicio11():
    return "TODO"

# 12. Escriba un programa que acepte una serie de números, con varios repetidos. La salida debe
# indicar la serie sin repetidos, la longitud de la serie y ordenada en orden creciente. Ejemplo,
# si recibe en la entrada [0, 3, 0, 1, 1, 1, 4, 2, 2, 3, 2, 3, 4], La salida debe ser [0, 1, 2, 3, 4] e
# indicar que su longitud es 5.

def ejercicio12(numbers=[0, 3, 0, 1, 1, 1, 4, 2, 2, 3, 2, 3, 4]):
    nonRepeatedNums = []
    for num in sorted(numbers):
        if (num not in nonRepeatedNums):
            nonRepeatedNums.append(num)
    print(
        f"Sin valores repetidos la longitud de la lista es de: {len(nonRepeatedNums)}")
    return nonRepeatedNums

# 13. Escriba un programa que reciba un párrafo de texto, y por la salida indique cuantos
# caracteres tiene originalmente, elimine las vocales, imprima el párrafo resultante e indique
# cuantos caracteres tiene el nuevo párrafo

def ejercicio13(parragraph: str = "Lorem ipsum"):
    filteredParragraph = parragraph
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in parragraph.lower():
        if x in vowels:
            filteredParragraph = filteredParragraph.replace(x, "")
    print(f"El párrafo original posee {len(parragraph)} carácteres")
    print(f"El párrafo sin vocales posee {len(filteredParragraph)} carácteres")
    return filteredParragraph


# 14. Escriba un programa que dada un dirección IPv4 válida retorne un versión deformada de
# esa dirección. Una versión de una dirección IP deformada reemplaza cada “.” con “[ . ]”.
# Ejemplo, entrada: dirección “255.100.50.0”, salida: “255[ . ]100[ . ]50[ . ]0”

def ejercicio14(ip: str = '0.0.0.0'):
    return "[ . ]".join(ip.split('.'))

# 15. Escriba un programa que acepte un número entero n y calcule el valor de n + nn + nnn,
# Por ejemplo, sea n = 5, la salida debe ser 615

def ejercicio15(num: int = 0):
    nums = num, f"{str(num)}{str(num)}", f"{str(num)}{str(num)}{str(num)}"
    res = 0
    for number in nums:
        res += int(number)
    return res
