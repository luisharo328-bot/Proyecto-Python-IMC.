# Link : https://github.com/luisharo32/Proyecto-Python-IMC
# Proyecto Calculadora IMC
nombre = input("Ingrese su nombre").title()
apellido = input(" Ingrese su apellido").title()
edad = input("Ingrese tu edad:")
peso = float(input("Ingrese su peso en kg:"))
estatura = float(input("Ingrese su estatura en metros:"))


imc = peso / (estatura ** 2)

print(f"Paciente: {nombre} {apellido}")
print(f"Edad : {edad}")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"Tu IMC: {imc:.2f}")
