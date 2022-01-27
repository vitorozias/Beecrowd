#recebendo três variaveis em uma linha só
linha1 = input().split()

a, b, c = linha1

#convertendo o formato de cada variável em float
a= float(a)
b= float(b)
c= float(c)

#descobrindo o maior numero entre os três
maior = (a+b+abs(a-b))/2
maior = (maior+c+abs(maior-c))/2

#mostrando o maior deles com 0 numeros depois da virgula
print ("%.0f eh o maior" %(maior))