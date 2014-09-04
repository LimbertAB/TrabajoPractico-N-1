cadena = raw_input("Introduce la cadena\n")
print(len(cadena))
cont = 0
cadena2="";
es = 1
for i in cadena:
  if i.isupper():
      i = i.lower()
  if i != " ":
      cadena2 = cadena2 + i
      cont = cont + 1
 
for i in range(cont/2):
  if cadena2[i] != cadena2[cont-i-1]:
      es = 0
      break
 
if (es):
  print "es palindromo"
else:
  print "no es palindromo"