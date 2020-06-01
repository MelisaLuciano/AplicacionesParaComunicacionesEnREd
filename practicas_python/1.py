nomb = "Melisa"
edad = 21

print(f"Hola {nomb} tienes {edad}")

nombre = input("Ingrese su nombre: ")
print(f"Holis {nombre}")

numero = int(input("Ingresa un numero: "))
print(f"El numero es: {numero + 1}")

#Funciones integradas
n = str(10.80)
print(n)

m = bin(10)
print(m)

h = hex(10)
print(h)

d = int("0b1010", 2)
print(d)

r = round(5.6)
print(r)

nn = len("Melisa")
print(nn)

a = float(input("Valor para a: "))
b = float(input("Valor para b: "))
c = float(input("Valor para c: "))

res = (a**3 * (b**2 - 2* a*c))/(2*b)
print(f"El resultado es: {res}")