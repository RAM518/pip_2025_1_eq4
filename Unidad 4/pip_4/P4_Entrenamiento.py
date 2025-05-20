import numpy as np
import random

archivo = "Instancias.txt"

with open(archivo, "r") as f:
    lineas = f.readlines()

# Primeras 3 líneas: n_instancias, n_entradas, n_salidas
n_instancias = int(lineas[0].strip())
n_entradas = int(lineas[1].strip())
n_salidas = int(lineas[2].strip())

# Procesamiento de datos
entradas = [list(map(float, lineas[i].strip().split())) for i in range(3, 3 + n_entradas)]
salidas = [list(map(float, lineas[i].strip().split())) for i in range(3 + n_entradas, 3 + n_entradas + n_salidas)]

# Transponer matrices
X = np.array(entradas).T  # Shape: (60, 4)
Y = np.array(salidas).T  # Shape: (60, 3)

# Extraer etiquetas como clases (0 = Alta, 1 = Media, 2 = Baja)
y_clases = np.argmax(Y, axis=1)


# --- Implementación manual de Counter ---
def contar_clases(y):
    conteo = {}
    for clase in y:
        conteo[clase] = conteo.get(clase, 0) + 1
    return conteo


conteo_clases = contar_clases(y_clases)
total = sum(conteo_clases.values())

print("Distribución de clases:")
for clase, cantidad in conteo_clases.items():
    nombre = ["Alta", "Media", "Baja"][clase]
    proporcion = cantidad / total * 100
    print(f"- {nombre}: {cantidad} instancias ({proporcion:.2f}%)")


# --- Implementación manual de train_test_split estratificado ---
def split_estratificado(X, Y, y, test_size=0.2, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)

    # Separar índices por clase
    indices_por_clase = {}
    for idx, clase in enumerate(y):
        if clase not in indices_por_clase:
            indices_por_clase[clase] = []
        indices_por_clase[clase].append(idx)

    # Mezclar índices de cada clase
    for clase in indices_por_clase:
        random.shuffle(indices_por_clase[clase])

    # Seleccionar muestras para test de cada clase
    test_indices = []
    for clase, indices in indices_por_clase.items():
        n_test = int(len(indices) * test_size)
        test_indices.extend(indices[:n_test])

    # Seleccionar muestras para train (el resto)
    train_indices = [i for i in range(len(y)) if i not in test_indices]

    # Mezclar los conjuntos finales
    random.shuffle(train_indices)
    random.shuffle(test_indices)

    return X[train_indices], X[test_indices], Y[train_indices], Y[test_indices]


# Dividir en entrenamiento (80%) y prueba (20%)
X_train, X_test, Y_train, Y_test = split_estratificado(X, Y, y_clases, test_size=0.4, random_seed=42)

print(f"\nTamaño del conjunto de entrenamiento: {len(X_train)}")
print(f"Tamaño del conjunto de prueba: {len(X_test)}")