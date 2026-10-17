# qml/benchmark_vs_svm.py - DEMO 2: VQC vs SVM (kernel RBF) con matriz de confusión y tiempos
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))   # permite ejecutar este archivo directamente
import time
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import numpy as np
from qml.datos import generar_lunas
from qml.modelo_vqc import escalar_y_dividir, crear_vqc, a_etiquetas

ETIQUETAS = ['Clase 0', 'Clase 1']

# Escalado a [0, pi/2] y ansatz EfficientSU2: la combinación que mejor aprendió en las pruebas
RANGO_LUNAS = (0, np.pi / 2)


def ejecutar_benchmark():
    X, y = generar_lunas()
    _, X_train, X_test, y_train, y_test = escalar_y_dividir(X, y, rango=RANGO_LUNAS)

    print('--- Entrenando SVM clásica (kernel RBF) ---')
    t0 = time.perf_counter()
    svm = SVC(kernel='rbf', C=1.0, gamma='scale')
    svm.fit(X_train, y_train)
    y_pred_svm = svm.predict(X_test)
    tiempo_svm = time.perf_counter() - t0
    acc_svm = svm.score(X_test, y_test)

    print('--- Entrenando modelo cuántico VQC ---')
    t0 = time.perf_counter()
    vqc = crear_vqc(X_train.shape[1], maxiter=200, entanglement='linear', ansatz_tipo='su2', reps_ansatz=3)
    vqc.fit(X_train, y_train)
    y_pred_vqc = a_etiquetas(vqc.predict(X_test))
    tiempo_vqc = time.perf_counter() - t0
    acc_vqc = vqc.score(X_test, y_test)

    print('=' * 50)
    print(' RESULTADOS DEL BENCHMARK')
    print('=' * 50)
    print(f'SVM clásica (RBF) -> tiempo: {tiempo_svm:.4f} s | exactitud test: {acc_svm * 100:.2f}%')
    print(f'VQC cuántico      -> tiempo: {tiempo_vqc:.4f} s | exactitud test: {acc_vqc * 100:.2f}%')
    print('=' * 50)
    print('Reporte de clasificación - SVM clásica:')
    print(classification_report(y_test, y_pred_svm, target_names=ETIQUETAS))
    print('Reporte de clasificación - VQC cuántico:')
    print(classification_report(y_test, y_pred_vqc, target_names=ETIQUETAS))

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred_svm), display_labels=ETIQUETAS).plot(
        ax=axes[0], cmap='Blues', colorbar=False)
    axes[0].set_title(f'SVM clásica (RBF) | {tiempo_svm:.3f} s | Acc {acc_svm * 100:.1f}%')
    ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred_vqc), display_labels=ETIQUETAS).plot(
        ax=axes[1], cmap='Purples', colorbar=False)
    axes[1].set_title(f'VQC cuántico | {tiempo_vqc:.3f} s | Acc {acc_vqc * 100:.1f}%')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    ejecutar_benchmark()
