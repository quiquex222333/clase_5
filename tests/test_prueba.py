import pytest

def test_suma(five, two):
    print(five)
    assert five + two == 7, "La suma no es correcta"

def test_resta(five):
    assert five - 2 == 3, "La resta no es correcta"

def test_multiplicacion(five, two):
    assert five * two == 10, "La multiplicacion no es correcta"
