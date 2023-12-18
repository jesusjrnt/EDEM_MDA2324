"""
A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:
2. Crea una función que pueda evaluar si un número (pasado por parámetro) es 
primo o no
"""

numero = int(input('¿Qué número quieres saber si es primo? '))


def es_primo:
    if numero < 2:
     False
    elif numero == 2:
        True
    else:
        es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print (f'{numero} es primo')
    else:
        print (f'{numero} no es primo')

