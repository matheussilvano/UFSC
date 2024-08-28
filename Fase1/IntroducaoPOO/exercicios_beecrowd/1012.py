(a, b, c)  = map(float, input().split(' '))
area_triangulo = a * c / 2
area_ciculo = 3.14159 * c**2
area_trapezio = ((a + b) * c) / 2
area_quadrado = b **2
area_retangulo = a * b
print(f'''TRIANGULO: {area_triangulo:.3f}
CIRCULO: {area_ciculo:.3f}
TRAPEZIO: {area_trapezio:.3f}
QUADRADO: {area_quadrado:.3f}
RETANGULO: {area_retangulo:.3f}''')
