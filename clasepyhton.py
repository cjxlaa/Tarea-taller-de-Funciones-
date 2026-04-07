def estadisticas_notas(notas):
    if not notas: return 0, 0, 0
    promedio = sum(notas) / len(notas)
    return promedio, max(notas), min(notas)

def obtener_aprobados(estudiantes):
    return [est for est in estudiantes if est[1] >= 3.0]

agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono

def buscar_contacto(nombre):
    return agenda.get(nombre, "No encontrado")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]


inventario = [
    {"nombre": "Laptop", "precio": 1200, "cantidad": 5},
    {"nombre": "Mouse", "precio": 25, "cantidad": 10}
]

def valor_total_inventario(inv):
    return sum(p['precio'] * p['cantidad'] for p in inv)

print(f"Total: ${valor_total_inventario(inventario)}")

def frecuencia_palabras(lista):
    frecuencias = {}
    for palabra in lista:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

clima = {
    "Bogotá": [12, 15, 14, 18, 13, 11, 14],
    "Medellín": [22, 25, 24, 26, 23, 22, 25]
}

def reporte_temperaturas(datos):
    for ciudad, temps in datos.items():
        print(f"{ciudad} -> Max: {max(temps)}°C, Min: {min(temps)}°C")

def calificar_estudiantes(estudiantes):
    # Rangos: (Limite inferior, Letra)
    rangos = [(4.5, 'A'), (4.0, 'B'), (3.5, 'C'), (3.0, 'D'), (0.0, 'F')]
    reporte = {}
    
    for nombre, nota in estudiantes:
        for limite, letra in rangos:
            if nota >= limite:
                reporte[nombre] = letra
                break
    return reporte

carrito = []

def agregar_al_carrito(nombre, precio):
    carrito.append({"nombre": nombre, "precio": precio})

def calcular_pago(descuento=0):
    subtotal = sum(item['precio'] for item in carrito)
    total = subtotal * (1 - descuento / 100)
    return total

productos_cat = [("Manzana", "Fruta"), ("Pollo", "Carne"), ("Pera", "Fruta")]

def agrupar_por_categoria(lista):
    agrupados = {}
    for prod, cat in lista:
        if cat not in agrupados:
            agrupados[cat] = []
        agrupados[cat].append(prod)
    return agrupados

votos_recibidos = ["Ana", "Luis", "Ana", "Nulo", "Luis", "Ana", "Viciado"]
candidatos_validos = ["Ana", "Luis", "Marta"]

def procesar_votos(votos, validos):
    conteo = {c: 0 for c in validos}
    invalidos = 0
    
    for v in votos:
        if v in conteo:
            conteo[v] += 1
        else:
            invalidos += 1
            
    total_validos = sum(conteo.values())
    ganador = max(conteo, key=conteo.get)
    porcentaje = (conteo[ganador] / total_validos) * 100 if total_validos > 0 else 0
    
    return ganador, porcentaje, invalidos
