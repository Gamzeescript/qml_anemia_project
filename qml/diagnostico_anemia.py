# qml/diagnostico_anemia.py - DEMO 1: diagnóstico de anemia con VQC (datos sintéticos de hemograma)
# Uso: python -m qml.diagnostico_anemia [--mapa z|zz]
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))   # permite ejecutar este archivo directamente
import argparse
import numpy as np
from qml.datos import generar_datos_anemia, DIAGNOSTICOS
from qml.modelo_vqc import escalar_y_dividir, crear_vqc, a_etiquetas

# Con RZ(2x) tras la Hadamard, la fase es 2x: escalar a [0, pi/2] mantiene la fase en [0, pi],
# un rango monótono que el ansatz puede leer. Con [0, 2*pi] la fase da dos vueltas y confunde al modelo.
RANGO = (0, np.pi / 2)


def ejecutar_diagnostico_qml(mapa='z'):
    nombre = 'ZFeatureMap (sin entrelazamiento)' if mapa == 'z' else 'ZZFeatureMap (con entrelazamiento)'
    print('=' * 56)
    print(' DEMO 1: DIAGNÓSTICO DE ANEMIA CON QML (VQC)')
    print(f' Feature map: {nombre}')
    print('=' * 56)

    X, y = generar_datos_anemia()
    scaler, X_train, X_test, y_train, y_test = escalar_y_dividir(X, y, estratificar=True, rango=RANGO)

    # q0 = Hb, q1 = VCM
    vqc = crear_vqc(num_qubits=2, maxiter=100, entanglement='full', mapa=mapa)

    print('[+] Entrenando el modelo de clasificación...')
    vqc.fit(X_train, y_train)
    print(f'[OK] Exactitud en entrenamiento: {vqc.score(X_train, y_train) * 100:.2f}%')
    print(f'[OK] Exactitud en prueba: {vqc.score(X_test, y_test) * 100:.2f}%')

    paciente = np.array([[8.5, 110.0]])
    pred = a_etiquetas(vqc.predict(scaler.transform(paciente)))
    print('[Paciente] Hb = 8.5 g/dL, VCM = 110 fL')
    print(f'[Resultado cuántico] {DIAGNOSTICOS[int(pred[0])]}')
    if mapa == 'zz':
        print('Nota: aquí las clases se separan solo por VCM; el entrelazamiento no aporta y puede estorbar.')
    print('Aviso: demo educativo con datos sintéticos; no es una herramienta de diagnóstico.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mapa', choices=['z', 'zz'], default='z')
    ejecutar_diagnostico_qml(parser.parse_args().mapa)
