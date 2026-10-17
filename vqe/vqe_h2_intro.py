# vqe/vqe_h2_intro.py - VQE introductorio: estado fundamental de H2 (proxy del enlace)
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))   # permite ejecutar este archivo directamente
from vqe.motor_vqe import energia_de_geometria


def simular_h2():
    print('1. Configurando la geometría (H2, distancia 0.735 Å)...')
    print('2. Calculando el estado fundamental con VQE...')
    qubits, e_elec, e_total = energia_de_geometria('H 0 0 0; H 0 0 0.735', espacio_activo=None)
    print(f'Número de qubits requeridos: {qubits}')
    print('=== Resultados ===')
    print(f'Energía electrónica: {e_elec:.6f} Hartree')                   # referencia: ~ -1.857
    print(f'Energía total (con repulsión nuclear): {e_total:.6f} Hartree')  # referencia: ~ -1.137
    return e_total


if __name__ == '__main__':
    simular_h2()
