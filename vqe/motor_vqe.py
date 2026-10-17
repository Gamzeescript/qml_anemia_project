# vqe/motor_vqe.py - pipeline VQE reutilizable: PySCF > espacio activo > Jordan-Wigner > UCCSD > VQE
# Si PySCF no está instalado (p. ej. Windows nativo), usa las integrales precalculadas de datos_precalculados.json
import json
import os
from pathlib import Path

import numpy as np
from qiskit.quantum_info import SparsePauliOp
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.transformers import ActiveSpaceTransformer
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit_nature.second_q.circuit.library import UCCSD, HartreeFock
from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import SLSQP
from common.compat import Estimator

ARCHIVO_PRECALCULADO = Path(__file__).with_name('datos_precalculados.json')


def clave_caso(coordenadas, espacio_activo):
    return f'{coordenadas.strip()}|{espacio_activo}'


def pyscf_disponible():
    # QML_SIN_PYSCF=1 fuerza el modo precalculado (útil para probarlo)
    if os.environ.get('QML_SIN_PYSCF') == '1':
        return False
    try:
        import pyscf  # noqa: F401
    except ImportError:
        return False
    return True


def resolver_operador(qubit_op, num_spatial_orbitals, num_particles, constante, maxiter=100):
    # Devuelve (num_qubits, energía electrónica, energía total) en Hartree
    mapper = JordanWignerMapper()
    init_state = HartreeFock(num_spatial_orbitals, num_particles, mapper)
    ansatz = UCCSD(num_spatial_orbitals, num_particles, mapper, initial_state=init_state)
    vqe = VQE(estimator=Estimator(), ansatz=ansatz, optimizer=SLSQP(maxiter=maxiter))
    resultado = vqe.compute_minimum_eigenvalue(qubit_op)
    e_elec = resultado.eigenvalue.real
    # eigenvalue es solo la parte electrónica: sumamos las constantes (repulsión nuclear, núcleo inactivo)
    return qubit_op.num_qubits, e_elec, e_elec + constante


def resolver_vqe(problem, maxiter=100):
    qubit_op = JordanWignerMapper().map(problem.hamiltonian.second_q_op())
    constante = sum(problem.hamiltonian.constants.values())
    return resolver_operador(qubit_op, problem.num_spatial_orbitals, problem.num_particles,
                             constante, maxiter)


def _desde_precalculado(coordenadas, espacio_activo, maxiter):
    datos = {}
    if ARCHIVO_PRECALCULADO.exists():
        datos = json.loads(ARCHIVO_PRECALCULADO.read_text(encoding='utf-8'))
    caso = datos.get(clave_caso(coordenadas, espacio_activo))
    if caso is None:
        raise RuntimeError('Esta geometría requiere PySCF (Linux, macOS, WSL o Colab). '
                           'Sin PySCF solo están disponibles las geometrías de vqe/geometrias.py.')
    print('    (PySCF no disponible: usando integrales precalculadas)')
    coefs = np.array([complex(re, im) for re, im in caso['coeficientes']])
    qubit_op = SparsePauliOp(caso['paulis'], coefs)
    return resolver_operador(qubit_op, caso['orbitales'], tuple(caso['particulas']),
                             caso['constante'], maxiter)


def energia_de_geometria(coordenadas, espacio_activo=(2, 2), maxiter=100, **opciones_driver):
    # espacio_activo = (electrones, orbitales espaciales); None usa el espacio completo
    if not pyscf_disponible():
        return _desde_precalculado(coordenadas, espacio_activo, maxiter)
    driver = PySCFDriver(atom=coordenadas, basis='sto3g', **opciones_driver)
    problem = driver.run()
    if espacio_activo is not None:
        transformer = ActiveSpaceTransformer(num_electrons=espacio_activo[0],
                                             num_spatial_orbitals=espacio_activo[1])
        problem = transformer.transform(problem)
    return resolver_vqe(problem, maxiter)
