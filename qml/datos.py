# qml/datos.py - datos sintéticos para los demos de clasificación
import numpy as np
from sklearn.datasets import make_moons

DIAGNOSTICOS = {
    0: 'Anemia microcítica (ferropénica / talasemia)',
    1: 'Anemia macrocítica (megaloblástica)',
}


def generar_datos_anemia(n_samples=60):
    # Hb en g/dL y VCM en fL. Clase 0 = microcítica, clase 1 = macrocítica
    np.random.seed(42)
    mitad = n_samples // 2
    x_micro = np.column_stack((np.random.uniform(7.0, 11.0, mitad), np.random.uniform(60.0, 78.0, mitad)))
    x_macro = np.column_stack((np.random.uniform(7.0, 11.0, mitad), np.random.uniform(102.0, 120.0, mitad)))
    X = np.vstack((x_micro, x_macro))
    y = np.concatenate((np.zeros(mitad, dtype=int), np.ones(mitad, dtype=int)))
    return X, y


def generar_lunas(n_samples=100):
    # Dataset no lineal (dos lunas)
    return make_moons(n_samples=n_samples, noise=0.15, random_state=42)
