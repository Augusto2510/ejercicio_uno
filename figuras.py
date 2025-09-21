
from math import pi, sqrt

def rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

def circulo(radio):
    area = pi * radio * radio
    perimetro = 2 * pi * radio
    return area, perimetro

def triangulo(base, altura):
    area = (base * altura) / 2
    hip = sqrt(base**2 + altura**2)
    perimetro = base + altura + hip
    return area, perimetro

