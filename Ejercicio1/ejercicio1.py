
print"INCISO A"
fn = 1
while fn <= 20: 
    print fn,
    fn += 1
print""
print"INCISO B"
fn = 20
while fn >=1: 
    print fn,
    fn -= 1
print""

print"INCISO C"
def Sumar():
    media = (a + b)
    print "La suma de los dos numeros es: ", media
    return

a = input('ingrese el primer numero')
b = input('ingrese el segundo numero')
Sumar()
print""

print"INCISO D"
def Sumar2():
    concatenacion=(str(num1))+(str(num2))
    print("concatenando el numero tenemos:  "),concatenacion
    return

num1=input('ingrese num1: ')
num2=input('ingrese num2: ')
Sumar2()
print""

print"INCISO E"
def Sumar3():
    media = (x + y)
    print "La suma de los dos numeros es: ", media
    return

x = input('ingrese x')
y = input('ingrese y')
Sumar3()
print""
print("Programa terminado")