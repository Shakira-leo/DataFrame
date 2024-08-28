import numpy as np
import pandas as pd

# Generar un array de 5 números aleatorios entre 1 y 10
numeros_aleatorios = np.random.randint(1, 11, size=5)

# Crear un DataFrame con la columna 'Numeros'
df_numeros = pd.DataFrame({'Numeros': numeros_aleatorios})

# Añadir la columna 'Dobles' con el doble de cada número
df_numeros['Dobles'] = df_numeros['Numeros'] * 2

# Mostrar el DataFrame final
print("DataFrame con números aleatorios y sus dobles:")
print(df_numeros)
