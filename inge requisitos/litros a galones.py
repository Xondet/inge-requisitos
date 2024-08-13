LITROS_POR_GALON = 3.785

litros_producidos = float(input("Ingrese la cantidad de litros producidos: "))

precio_por_galon = float(input("Ingrese el precio por galón: "))

galones_producidos = litros_producidos / LITROS_POR_GALON

total_recibido = galones_producidos * precio_por_galon

print(f"El productor recibirá ${total_recibido:.2f} por la producción de {litros_producidos} litros.")