horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))

pago_por_hora = float(input("Ingrese el pago por hora: "))

sueldo_semanal = horas_trabajadas * pago_por_hora

print(f"El sueldo semanal del trabajador es: ${sueldo_semanal:.2f}")