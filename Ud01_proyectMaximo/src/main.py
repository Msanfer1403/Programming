EUR_TO_USD = 1.08  

euros = float(input("Introduce la cantidad en EUR (€): "))
dolares = euros * EUR_TO_USD
print(f"{euros:.2f} EUR equivalen a {dolares:.2f} USD (Tasa: {EUR_TO_USD})")