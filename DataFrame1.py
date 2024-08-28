import pandas as pd

# Diccionario de datos
datos = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Marta'],
    'Edad': [15, 14, 16, 15],
    'Nota': [8.5, 9.0, 7.5, 8.0],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia','Sevilla']
}

# DataFrame usando el diccionario
df = pd.DataFrame(datos)

# El DataFrame
print("DataFrame de estudiantes:")
print(df)