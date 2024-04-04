def area_triangulo_retangulo(base, altura):
    return (base * altura) / 2


def area_circulo(raio):
    pi = 3.14159
    return pi * (raio ** 2)


def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2


def area_quadrado(lado):
    return lado ** 2


def area_retangulo(lado1, lado2):
    return lado1 * lado2

A, B, C = map(float, input().split())

print("TRIANGULO: {:.3f}".format(area_triangulo_retangulo(A, C)))
print("CIRCULO: {:.3f}".format(area_circulo(C)))
print("TRAPEZIO: {:.3f}".format(area_trapezio(A, B, C)))
print("QUADRADO: {:.3f}".format(area_quadrado(B)))
print("RETANGULO: {:.3f}".format(area_retangulo(A, B)))
