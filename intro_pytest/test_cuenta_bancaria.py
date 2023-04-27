import pytest

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, cantidad):
        self.saldo += cantidad
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No tienes suficiente saldo")
        self.saldo -= cantidad
    def consultar_saldo(self):
        print(f"saldo {self.saldo}")
        return self.saldo
""""
    En el método setup_method, crea una nueva instancia de la clase
    CuentaBancaria y guárdala en una variable de instancia
"""
class TestCuentaBancaria:
    def setup_method(self):
        self.cuenta = CuentaBancaria("Alina", 100)

    def test_depositar(self):
        self.cuenta.depositar(20)
        assert self.cuenta.consultar_saldo() == 120, "El saldo debe ser 120 despues de depositar 20"

    def test_retirar(self):
        self.cuenta.retirar(50)
        assert self.cuenta.consultar_saldo() == 50, "El saldo debe ser 70 despues de retirar 50"
    def test_retirar_insuficiente(self):
        try:
            self.cuenta.retirar(120)
            assert False
        except Exception:
            assert True, "El saldo es insuficiente"

    def teardown_method(self):
        print("*" * 80)
        print(f"TEARDOWN SETUP")
        print("*" * 80)


"""
En el método teardown_method, no es necesario hacer nada, ya que no hay
nada que limpiar después de cada prueba.
"""


""""
    def test_invalid_logic(self):
        print("Invalid login test")

    def teardown_method(self):
        print("*" * 80)
        print(f"TEARDOWN SETUP - Cerrar el navegador")
        print("*" * 80)

    @classmethod
    def teardown_class(cls):
        print("*" * 80)
        print(f"TEARDOWN SETUP - Limpiar usuarios con llamadas a DB")
        print("*" * 80)

"""
