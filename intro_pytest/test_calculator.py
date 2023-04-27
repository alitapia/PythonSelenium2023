"""1. Crea un archivo llamado "test_calculator.py".
2. Importa la biblioteca pytest al principio del archivo.
3. Crea una función llamada "test_suma" que use la función suma de la
calculadora para sumar dos números y verificar que el resultado es correcto
utilizando la aserción assert.
4. Crea otra función llamada "test_resta" que use la función resta de la
calculadora para restar dos números y verificar que el resultado es correcto
utilizando la aserción assert.
5. Crea una tercera función llamada "test_multiplicacion" que use la función
multiplicación de la calculadora para multiplicar dos números y verificar que
el resultado es correcto utilizando la aserción assert.
6. Crea una cuarta función llamada "test_division" que use la función división de
la calculadora para dividir dos números y verificar que el resultado es correcto
utilizando la aserción assert.
7. Ejecuta el archivo
"""

import pytest
class Calculadora:
    def __init__(self):
        pass
    def suma(self, num_a: int, num_b: int):
        return num_a + num_b
    def resta(self, num_a: int, num_b: int):
        return num_a - num_b
    def multiplicacion(self, num_a: int, num_b:int):
        return num_a * num_b
    def division(self, num_a: int, num_b: int):
        return num_a // num_b #si quiero flotantes solo un /


def test_suma():
    calcula = Calculadora()
    resultado = calcula.suma(1, 2)
    assert resultado == 3, "la funcion suma debe regresar 3 para 1 y 2"

def test_resta():
    calcula = Calculadora()
    resultado = calcula.resta(2, 1)
    assert resultado == 1, "la funcion resta debe regresar 1 para 2 y 1"


def test_multiplicacion():
    calcula = Calculadora()
    resultado = calcula.multiplicacion(2, 1)
    assert resultado == 2, "la funcion multiplicacion debe regresar 1 para 2 y 1"


def test_division():
    calcula = Calculadora()
    resultado = calcula.division(2, 1)
    assert resultado == 2, "la funcion division debe regresar 2 para 2 y 1"
