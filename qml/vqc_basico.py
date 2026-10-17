# qml/vqc_basico.py - VQC introductorio sobre datos sintéticos (make_blobs)
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))   # permite ejecutar este archivo directamente
import numpy as np
from sklearn.datasets import make_blobs
from qml.modelo_vqc import escalar_y_dividir, crear_vqc


def ejecutar_vqc_basico():
    print('1. Generando dataset sintético (2 características, 2 clases)...')
    X, y = make_blobs(n_samples=50, centers=2, n_features=2, random_state=42, cluster_std=1.2)
    _, X_train, X_test, y_train, y_test = escalar_y_dividir(X, y, estratificar=True, rango=(0, np.pi / 2))
    print(f'Dimensiones de entrada: {X_train.shape[1]} qubits')

    perdidas = []

    def callback(pesos, valor):
        perdidas.append(valor)
        print(f'Iteración {len(perdidas)}: pérdida = {valor:.4f}')

    vqc = crear_vqc(X_train.shape[1], maxiter=100, callback=callback, mapa='z')
    print('2. Entrenando el Variational Quantum Classifier (VQC)...')
    vqc.fit(X_train, y_train)
    print('=== Resultados del modelo QML ===')
    print(f'Exactitud en entrenamiento: {vqc.score(X_train, y_train) * 100:.2f}%')
    print(f'Exactitud en prueba: {vqc.score(X_test, y_test) * 100:.2f}%')


if __name__ == '__main__':
    ejecutar_vqc_basico()
