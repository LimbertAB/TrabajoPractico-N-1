nombre = raw_input()
nombre2= raw_input()
aux=len(nombre)
aux2=len(nombre2)
if aux>aux2:
	print nombre 
else :
	if aux2>aux:
		print nombre2
	else :
		concatenacion=(str(nombre))+(str(nombre2))
		print concatenacion
