import pandas as pd

# Datos embebidos del archivo "MM Data.csv"
data = pd.DataFrame({
        "Red": [3, 4, 4, 4, 5, 6, 7, 5, 8, 2, 9, 5, 10, 6, 5, 3, 8, 7, 6, 4, 2, 9, 3, 8, 9, 2, 3, 7, 6, 4],
    "Green": [5, 2, 6, 6, 5, 6, 8, 5, 7, 4, 8, 7, 3, 9, 5, 3, 4, 5, 6, 2, 3, 6, 7, 9, 8, 4, 3, 4, 7, 2],
    "Blue": [11, 10, 9, 7, 16, 8, 11, 9, 7, 5, 6, 11, 12, 8, 14, 6, 11, 7, 6, 7, 8, 7, 6, 6, 5, 9, 4, 8, 9, 7],
    "Orange": [12, 6, 4, 6, 12, 10, 6, 7, 5, 6, 8, 7, 4, 5, 6, 6, 6, 8, 9, 4, 5, 7, 6, 5, 8, 4, 6, 7, 5, 5],
    "Yellow": [11, 18, 12, 14, 7, 9, 10, 12, 11, 13, 15, 12, 11, 13, 9, 10, 12, 10, 11, 14, 12, 14, 13, 12, 12, 9, 11, 10, 11, 10],
    "Brown": [16, 18, 20, 19, 12, 17, 11, 9, 15, 10, 14, 11, 12, 14, 13, 14, 12, 13, 14, 11, 10, 11, 12, 13, 12, 10, 14, 14, 15, 12],
    "Weight": [48.72, 48.45, 48.33, 46.72, 48.95, 47.85, 46.78, 47.55, 48.32, 47.12,
                46.88, 48.65, 48.11, 47.25, 46.99, 47.44, 48.35, 47.98, 47.65, 46.79,
                47.29, 47.82, 47.99, 48.45, 48.36, 46.77, 48.09, 47.45, 48.03, 47.15]
})

# Número total de bolsas
total_bags = len(data)

# Agregar columna Total (suma de colores)
data['Total'] = data[['Red', 'Green', 'Blue', 'Orange', 'Yellow', 'Brown']].sum(axis=1)

# Evento R: Bolsas con al menos 10 botonetas rojas
R = data['Red'] >= 10
P_R = R.sum() / total_bags

# Evento T: Bolsas con al menos 57 botonetas en total
T = data['Total'] >= 57
P_T = T.sum() / total_bags

# Evento W: Bolsas que pesan al menos 50 gramos
W = data['Weight'] >= 50
P_W = W.sum() / total_bags

# Intersección R ∩ T: Bolsas con al menos 10 botonetas rojas y 57 botonetas en total
R_intersection_T = (R & T)
P_R_intersection_T = R_intersection_T.sum() / total_bags

# Diferencia T \ W: Bolsas con al menos 57 botonetas pero pesan menos de 50 gramos
T_difference_W = (T & ~W)
P_T_difference_W = T_difference_W.sum() / total_bags

print("Resultados del Análisis de Probabilidades:\n")
print(f"a) P(R) = {P_R:.4f}")
print(f"b) P(T) = {P_T:.4f}")
print(f"c) P(W) = {P_W:.4f}")
print(f"d) P(R ∩ T) = {P_R_intersection_T:.4f}")
print(f"e) P(T \\ W) = {P_T_difference_W:.4f}")
