## Recebendo a entrada das variáveis.
linha1 = input().split()
linha2 = input().split()

cp1,np1,vp1 = linha1
cp2,np2,vp2 = linha2
##Convertendo os valores das variaveis.
cp1= int(cp1)
np1= int(np1)
vp1= float(vp1)

cp2= int(cp2)
np2= int(np2)
vp2= float(vp2)

##Pagamento da Peça 1 e Peça 2.
res1= np1*vp1
res2= np2*vp2

total= res1+res2

print ("VALOR A PAGAR: R$ %.2f" %total)