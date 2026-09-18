"""
Sesion 6 - Taller de Laboratorio Final: El Experto Automatico (45 MIN)
Proyecto Integrador del Modulo 1: un arbol de decision aprende automaticamente
la Base de Conocimientos de un Sistema Experto de Marketing.
"""
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text

# Paso 2: Dataset simulado de Marketing
# Columnas (X): [Edad, Horas_Online, Compras_Previas]
X = np.array([
    [22, 5, 0],
    [45, 1, 3],
    [19, 8, 0],
    [35, 2, 5],
    [28, 6, 1],
    [50, 0, 4],
    [23, 7, 0],
    [40, 1, 6],
    [31, 4, 2],
    [55, 0, 5],
])

# Y: 1 = Hizo clic en el anuncio, 0 = Lo ignoro
# Patron buscado: jovenes con muchas horas online y pocas compras previas -> clic
Y = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])

# Paso 3: entrenamiento del arbol de decision
arbol = DecisionTreeClassifier(max_depth=3, random_state=42)
arbol.fit(X, Y)

# Paso 4: extraccion de las reglas en texto
nombres_variables = ["Edad", "Horas_Online", "Compras_Previas"]
reglas_texto = export_text(arbol, feature_names=nombres_variables)

if __name__ == "__main__":
    print("Base de Reglas generada automáticamente:\n")
    print(reglas_texto)
