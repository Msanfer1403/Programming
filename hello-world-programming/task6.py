print("OPERACIONES ARITMÉTICAS")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

print(f"\nResultados para {num1} y {num2}:")
print(f"1. Suma (+): {num1 + num2}")
print(f"2. Resta (-): {num1 - num2}")
print(f"3. Multiplicación (*): {num1 * num2}")

if num2 != 0:
    print(f"4. División (/): {num1 / num2:.2f}")
    print(f"5. División entera (//): {num1 // num2}")
    print(f"6. Módulo/Resto (%): {num1 % num2}")
else:
    print("4-6. No se puede dividir entre cero.")

print(f"7. Exponente (**): {num1 ** num2}\n")

print("CONVERSOR")

EUR_TO_USD = 1.08  

celsius = float(input("Introduce la temperatura en °C: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F\n")

euros = float(input("Introduce la cantidad en EUR (€): "))
dolares = euros * EUR_TO_USD
print(f"{euros:.2f} EUR equivalen a {dolares:.2f} USD (Tasa: {EUR_TO_USD})")