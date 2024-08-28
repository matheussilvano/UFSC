a = float(input())
b = float(input())
c = float(input())
area_triangulo = a * c / 2
area_ciculo = 3.14159 * c**2
area_trapezio = ((a + b) * c) / 2
area_quadrado = b **2
area_retangulo = a * b
print(f'''TRIANGULO: {area_triangulo:.3f}
CIRCULO = {area_ciculo:.3f}
TRAPEZIO = {area_trapezio:.3f}
QUADRADO = {area_quadrado:.3f}
RETANGULO = {area_retangulo:.3f}''')


# Traceback (most recent call last):
#  File "/judge/judge-6432b0e7ede6434ead08441207f90be1.d/Main.py", line 1, in <module>
#    a = float(input())
#        ^^^^^^^^^^^^^^
# ValueError: could not convert string to float: *******
#
# Esse erro não faz sentido, pois é possível declarar uma variável como float
