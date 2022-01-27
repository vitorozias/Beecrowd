#JEITO 01 (CORRETO PARA O SITE)
#pegar duas varíaveis na mesma linha
x = int(input())
y = float(input())

#calculando a média do consumo
media = x / y

#mostrando a média para o usuario utilizando três casas após a virgula
print ("%.3f km/l"% (media))

#JEITO 02 (FUNCIONA 100% MAS O SITE NAO ACEITA, POR PEGAR DOIS VALORES DE UMA VEZ SÓ)
#pegar duas varíaveis na mesma linha
linha1 = input().split()

#definindo para qual variavel as entradas irão
x, y = linha1

#definindo o tipo de varíavel
x = int(x)
y = float(y)

#calculando a média do consumo
media = x / y

#mostrando a média para o usuario utilizando três casas após a virgula
print ("%.3f km/l"% (media))
