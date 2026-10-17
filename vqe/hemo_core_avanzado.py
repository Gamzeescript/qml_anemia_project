import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))   # permite ejecutar este archivo directamente
from qiskit_nature.second_q.drivers import MethodType
from vqe.geometrias import HEMO_CORE_XYZ
from vqe.motor_vqe import energia_de_geometria, pyscf_disponible


def evaluar_nucleo_hemo():
    if not pyscf_disponible():
        print('Este script requiere PySCF (Linux, macOS, WSL o Colab); no está disponible en Windows nativo.')
        return None
    print('1. Cargando el núcleo activo del grupo hemo (modelo reducido)...')
    print('2. Espacio activo (3 alfa + 1 beta electrones, 4 orbitales); puede tardar varios minutos...')
    # Capa abierta (spin=2): método ROHF y electrones activos como tupla (alfa, beta)
    qubits, _, e_total = energia_de_geometria(
        HEMO_CORE_XYZ, espacio_activo=((3, 1), 4), charge=2, spin=2, method=MethodType.ROHF)
    print(f'Qubits requeridos: {qubits}')
    print(f'Energía total del núcleo Fe-N4-O: {e_total:.6f} Hartree')
    print('Una energía más baja en un diseño alternativo indica mayor estabilidad; no es una cura.')
    return e_total


if __name__ == '__main__':
    evaluar_nucleo_hemo()
