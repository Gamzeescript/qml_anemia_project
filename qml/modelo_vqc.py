# qml/modelo_vqc.py - piezas reutilizables del VQC: preparación de datos, modelo y utilidades
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from qiskit.circuit.library import ZFeatureMap, ZZFeatureMap, RealAmplitudes, EfficientSU2
from qiskit_algorithms.optimizers import COBYLA
from qiskit_algorithms.utils import algorithm_globals
from qiskit_machine_learning.algorithms import VQC
from common.compat import Sampler

algorithm_globals.random_seed = 42


def escalar_y_dividir(X, y, estratificar=False, rango=(0, 2 * np.pi)):
    # Los datos entran al circuito como ángulos: el rango de escalado importa (ver diagnostico_anemia.py)
    scaler = MinMaxScaler(feature_range=rango)
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=42, stratify=y if estratificar else None)
    return scaler, X_train, X_test, y_train, y_test


def crear_vqc(num_qubits, maxiter=80, entanglement='linear', callback=None, mapa='zz', ansatz_tipo='real', reps_ansatz=2):
    # mapa='zz': ZZFeatureMap (con entrelazamiento); mapa='z': ZFeatureMap (sin entrelazamiento)
    if mapa == 'z':
        feature_map = ZFeatureMap(feature_dimension=num_qubits, reps=1)
    else:
        feature_map = ZZFeatureMap(feature_dimension=num_qubits, reps=2, entanglement=entanglement)
    # RealAmplitudes: solo rotaciones RY (más simple); EfficientSU2: RY y RZ (más expresivo)
    constructor = EfficientSU2 if ansatz_tipo == 'su2' else RealAmplitudes
    ansatz = constructor(num_qubits=num_qubits, reps=reps_ansatz, entanglement='linear')
    return VQC(sampler=Sampler(), feature_map=feature_map, ansatz=ansatz,
               optimizer=COBYLA(maxiter=maxiter), callback=callback)


def a_etiquetas(pred):
    # VQC puede devolver etiquetas 1D o one-hot (2D): normalizamos a 1D
    pred = np.atleast_1d(np.asarray(pred))
    return pred.argmax(axis=1) if pred.ndim == 2 else pred
