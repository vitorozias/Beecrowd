# Ler três valores em apenas uma linha, sendo eles a, b, c
a, b, c = (input().split())

# Convertendo os valores para float
a = float (a)
b = float (b)
c = float (c)

# Fazendo a operação matemática para chegar aos resultados
triangulo = (a*c)/2

circulo = pow(c,2) * 3.14159

trapezio = ((a+b)/2) * c

quadrado = pow(b,2) 

retangulo = a*b

# Mostra os resultados com 3 números após a virgula.
print ("TRIANGULO: %.3f" % (triangulo))
print ("CIRCULO: %.3f" % (circulo))
print ("TRAPEZIO: %.3f" % (trapezio))
print ("QUADRADO: %.3f" % (quadrado))
print ("RETANGULO: %.3f" % (retangulo))