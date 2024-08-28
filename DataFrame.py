import pandas as pd

# Crear un diccionario con los datos
datos = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Marta'],
    'Edad': [15, 14, 16, 15],
    'Nota': [8.5, 9.0, 7.5, 8.0]
}

# Crear el DataFrame usando el diccionario
df = pd.DataFrame(datos)

# Mostrar el DataFrame
print("DataFrame de estudiantes:")
print(df)
