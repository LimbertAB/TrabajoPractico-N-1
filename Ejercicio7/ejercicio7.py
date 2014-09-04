altura = int(input("Altura de la figura: "))
into=1
aux1=1
aux2=1
while into<=altura:
	while aux1<=aux2:
			print(aux2),
			aux1+=1
	print ""
	aux2+=1
	aux1=1
	into+=1
altura-=1
aux1=altura
aux2=altura
while altura>=1:
	while aux1>=1:
			print(aux2),
			aux1-=1
	print ""
	aux2-=1
	aux1=aux2
	altura-=1