# Datos almacenados en un diccionario de listas
datos = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Marta'],
    'Edad': [15, 14, 16, 15],
    'Nota': [8.5, 9.0, 7.5, 8.0],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

# Función para imprimir el DataFrame manualmente
def imprimir_dataframe(datos):
    # Imprimir encabezados
    encabezados = list(datos.keys())
    print(f"{encabezados[0]:<10} {encabezados[1]:<5} {encabezados[2]:<5} {encabezados[3]:<10}")
    print("-" * 35)

    # Imprimir cada fila de datos
    for i in range(len(datos['Nombre'])):
        print(f"{datos['Nombre'][i]:<10} {datos['Edad'][i]:<5} {datos['Nota'][i]:<5} {datos['Ciudad'][i]:<10}")

# Mostrar el "DataFrame"
print("DataFrame de estudiantes:")
imprimir_dataframe(datos)
