nombre = "luis"
edad = 20
print(f"hola, soy {nombre} y tengo {edad} años")

nombre = "luis_1"
edad ="20"
print(f"hola {nombre} y tengo {20}")


# Conversiones de variables
numero_str = "100"

# a + b // a,b deben ser del mismo tipo ( decimal o enteros)
# No podemos sumar / concatenar un string con un entero directamente
print(f"{numero_str}50") # output 10050
numero_int = int(numero_str) + 50 # conversion de string a entero
print(numero_int)

fruits_str =["10","20","50"] # output [20,20,50]
print(fruits_str)
fruits_int = list(map(int,fruits_str))
print(fruits_int)


flotante = 10.56
entero = int(flotante)
print(entero)
print(int(round(flotante, 0))) #output 10

flotante_nuevo = float(numero_str )# convertir de entero a float
print((flotante_nuevo))# output 100.0
print(entero + flotante_nuevo) # output 110

# Boleanos , coversion
is_boolean = True
is_boolean_str = str(is_boolean) # convertir de booleano a string
print(is_boolean_str) # output True
is_boolean_int = int(is_boolean)#output 1
print(is_boolean_int)
is_boolean_float = float(is_boolean)# output 1.0
boolean_float = bool(numero_str)# output True
print(boolean_float)

fruta = "uva"
fruta_int = int(fruta)
print(fruta_int)# output error porque fruta no es un numero de base10