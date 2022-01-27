#recebendo dois valores de uma só vez (em cada linha)
linha1 = input("Digite x1 e y1: ").split()
linha2 = input("Digite x2 e y2: ").split()

#atribuindo os valores a cada variavel (sempre na ordem que foi solicitado no input de cima)
x1, y1 = linha1
x2, y2 = linha2

#definindo o tipo de variável para todas elas
x1= float(x1)
y1= float(y1)
x2= float(x2)
y2= float(y2)

#efetuando o calculo para saber a distancia entre eles
distancia= ((x2-x1)**2 + (y2-y1)**2)**(0.5)

#mostrando o resultado com quatro casas decimais
print ("%.4f"%(distancia))