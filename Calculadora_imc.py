# Proyecto python calculadora de IMC

nombre = input("ingrese su nombre")
edad = int(input("ingrese su edad"))
peso = float(input("ingrese su peso en kg"))
estatura = float(input("ingrese su estatura en metros"))

# formula de calculo de IMC
imc = peso / (estatura ** 2)
print(f"{nombre}, tienes {edad} años")
print(f"tu peso es {peso} en kg y tu estatura es {estatura} en metros")
print(f"tu IMC es: {imc:.2f}")
