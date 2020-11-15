import inspect

# 14/11/2020
# Angel Rodríguez
# CI: 27015036
# Realizado usando python 3.7.7


def parentFnCaller():
    return inspect.stack()[2][3]


def info():
    print("")
    print("-----------------------")
    print(" ".join(parentFnCaller().upper().split('_')))


def printInputOutput(input, output):
    print(f"Entrada: {input}")
    print(f"Salida: {output}")


# 1. Escriba un programa que reciba como entrada un número entero n mayor a 0, y la salida
# sea de la forma 123…n, donde … son los números que faltan en la secuencia. Ejemplo:
# Si la entrada n = 5, la salida es 12345

def ejercicio_1(n=5):
    info()
    for i in range(n):
        print(i+1, end=' ')

# 2. Escriba una función llamada rotate() que reciba como argumento una lista y un entero n y
# rote los elemento de la lista de acuerdo a ese número n. Ejemplo, lista de entrada: [1, 2, 3,
# 4, 5, 6 ] ; n= 2. La salida debe ser [3, 4, 5, 6, 1, 2]


def ejercicio_2(lista=[1, 2, 3, 4, 5, 6], number=2):
    info()

    def rotate(l, n):
        return l[n:] + l[:n]
    printInputOutput(lista, rotate(lista, number))

# 3. Escriba una función llamada delete_duplicates(), que reciba una lista con varios elemento
# duplicados y la salida sea la lista sin duplicados. Ejm: lista de entrada [12, 24, 12, 56, 3, 14,
# 56, 3, 12], la salida debe ser [12, 24, 56, 3, 14]


def ejercicio_3(l=[12, 24, 12, 56, 3, 14, 56, 3, 12]):
    info()

    def delete_duplicates(lista):
        return list(set(lista))
    printInputOutput(l, delete_duplicates(l))

# 4. Escriba un programa que dado tres tuples con nombres, edades y ciudades. Como entrada
# solicite un numero n y en la salida indique el nombre, edad y ciudad correspondiente a es
# número. Ejemplo:
# nombres = (“Juan”, “Maria”, “Ricardo”, “Ana”, “Cecilia”)
# edades = (23, 21, 19, 25, 22)
# ciudades = (“Maracay”, “Valencia”, “Caracas”, “Barquisimeto”, “Barcelona”)
# n = 2, la salida será: Ricardo 19 Caracas


def ejercicio_4(n=2):
    info()
    nombres = ("Juan", "Maria", "Ricardo", "Ana", "Cecilia")
    edades = (23, 21, 19, 25, 22)
    ciudades = ("Maracay", "Valencia", "Caracas", "Barquisimeto", "Barcelona")
    printInputOutput(n, f"{nombres[n]} {edades[n]} {ciudades[n]}")

# 5. Escriba un programa que dado una lista de tuples que representan un nombre y una edad,
# encontrar la persona de mayor edad. Ejm: [(“Antonio”, 21), (“Roberto”, 18), (“Teresa”, 19)],
# la salida debe ser: Antonio 21


def ejercicio_5(data=[("Antonio", 21), ("Roberto", 18), ("Teresa", 19)]):
    info()
    copy = data
    copy.sort(key=lambda x: x[1], reverse=True)
    printInputOutput(data, copy[0])

# 6. Escriba una función llamada find_indexes() que reciba como parámetro un string y un
# substring, y la salida sea un tuple que indique los índices de ocurrencia de ese substring en
# el primer string. Ejm, string = “tattattata” y el substring es “tt”, la salida debe ser (2, 5)


def ejercicio_6(string="tattattata", substring="tt"):
    info()

    def find_indexes(s, subs):
        return tuple([n for l in s if l.startswith(subs)])

    printInputOutput(
        f"String: {string}\nSubstring: {substring}", find_indexes(string, substring))

# 7. Escriba una función llamada sumNumbers(), que reciba como entrada un string que
# contiene caracteres numéricos y la salida muestre la suma de tales valores. Ejm: entrada:
# abc1234xyz, la salida debe ser 1234; entrada = aa11b33, salida 44; entrada: pueblo, salida 0.


def ejercicio_7(s="abc1234xyz"):
    info()

    def sumNumbers(string):
        temp = "0"
        total = 0
        for char in string:
            if (char.isdigit()):
                temp += char
            else:
                total += int(temp)
                temp = "0"
        return total + int(temp)
    printInputOutput(s, sumNumbers(s))

# 8. Escriba una función llamada primeOrComposite(), que reciba como argumento un número
# n positivo y la salida sea Primo si es primo o Compuesto si no lo es, Ejm: entrada 47, salida
# Primo, entrada 16, salida Compuesto


def ejercicio_8(number=16):
    info()

    def primeOrComposite(n):
        if (n <= 1):
            return "Primo"
        if (n <= 3):
            return "Primo"
        if (n % 2 == 0 or n % 3 == 0):
            return "Compuesto"
        i = 5
        while(i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return "Compuesto"
            i = i + 6
        return "Primo"
    printInputOutput(number, primeOrComposite(number))
    # TODO

# 9. Escriba una función que reciba como entrada una lista y la salida sea la lista con los
# elementos intercambiados, ejemplo: entrada: [1, 2, 3, 4, 5], salida: [2, 1, 4, 3, 5]


def ejercicio_9(lista=[1, 2, 3, 4, 5]):
    info()
    copy = lista.copy()
    for i in range(0, len(lista) - 1, 2):
        copy[i], copy[i+1] = lista[i+1], lista[i]
    printInputOutput(lista, copy)

# 10. La función zip() de Python, toma dos o más objetos iterables y retorna una lista de tuples
# con un elemento de cada lista de entrada, de acuerdo a su índice. Ejemplo entrada, paises
# = ["China", "India", "Estados Unidos", "Indonesia"] ; poblaciones = [1391, 1364, 327, 264].
# La salida es [('China', 1391), ('India', 1364), ('Estados Unidos', 327), ('Indonesia', 264)].
# Escriba una función llamada my_zip(), que realice lo mismo (limítelo a sólo dos iterables).


def ejercicio_10(paises=["China", "India", "Estados Unidos", "Indonesia"], poblaciones=[1391, 1364, 327, 264]):
    info()

    def my_zip(x, y):
        zipeado = []
        for i in range(len(x)):
            zipeado.append((x[i], y[i]))
        return zipeado
    printInputOutput(
        f"Paises: {paises}\nPoblaciones: {poblaciones}", my_zip(paises, poblaciones))

# 11. Escriba una función lambda que encuentre el valor de 𝑒^𝑥
# dada por la expresión ((1 + 1/n)^n)^x
# para un valor de n= 1000.


def ejercicio_11(x=5):
    info()
    n = 1000
    printInputOutput(x, (lambda x: ((1 + 1/n) * n) * x)(x))

# 12. Escriba una función lambda que obtenga el primer y último valor de una lista.


def ejercicio_12(l=[1, 2, 3, 4, 5]):
    info()
    printInputOutput(l, (lambda x: [x[0], x[len(x)-1]])(l))

# 13. Escriba un generador usando una compresión de lista para indicar en una lista de enteros
# cuales son pares y cuales impares, por ejemplo, entrada: [1, 2, 3 , 4] salida: [“impar”, “par”,
# “impar”, “par”]. Ayuda: recuerde la forma abreviada del if


def ejercicio_13(lista=[1, 2, 3, 4]):
    info()
    printInputOutput(lista, ["par" if n % 2 == 0 else "impar" for n in lista])

# 14. Escriba una función map, para que dada una lista con nombres, la salida sea la lista con los
# nombres en Mayúsculas. Ejm: entrada [“alfredo”, “luis”, “margarita”, “rosa”], salida
# [“ALFREDO”, “LUIS”, “MARGARITA”, “ROSA”]


def ejercicio_14(nombres=["alfredo", "luis", "margarita", "rosa"]):
    info()
    printInputOutput(nombres, list(map(lambda s: s.capitalize(), nombres)))

# 15. Escriba una función filter, que aplicada a una lista con notas de alumnos, devuelva a la salida
# una lista con aquellas notas superiores a 17. Ejm: entrada [13, 20, 15, 18, 12, 19, 14, 17,18]
# la salida debe ser [20, 18, 19, 18]


def ejercicio_15(notas=[13, 20, 15, 18, 12, 19, 14, 17, 18]):
    info()

    def filtrar_x_nota(nota):
        return nota > 17
    printInputOutput(notas, list(filter(filtrar_x_nota, notas)))

print("Angel Rodriguez, CI 27015036")
ejercicio_1()
ejercicio_2()
ejercicio_3()
ejercicio_4()
ejercicio_5()
ejercicio_6()
ejercicio_7()
ejercicio_7("aa11b33")
ejercicio_7("pueblo")
ejercicio_8()
ejercicio_9()
ejercicio_10()
ejercicio_11()
ejercicio_12()
ejercicio_13()
ejercicio_14()
ejercicio_15()
