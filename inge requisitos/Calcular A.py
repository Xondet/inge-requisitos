

def calcular_area(A, B, C):
    A = float(input("Ingrese el valor de A: "))
    B = float(input("Ingrese el valor de B: "))
    C = float(input("Ingrese el valor de C: "))
    altura_triangulo = A - C
    
    area_triangulo = 0.5 * B * altura_triangulo
    
    area_rectangulo = B * C
    
    area_total = area_triangulo + area_rectangulo
    
    return area_total
    area = calcular_area(A, B, C)
    print(f"El área total del terreno es: {area} unidades cuadradas")
