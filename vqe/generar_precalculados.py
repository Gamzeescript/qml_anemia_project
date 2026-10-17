# vqe/generar_precalculados.py - genera datos_precalculados.json (requiere PySCF: Linux, macOS, WSL o Colab)
# Uso: python -m vqe.generar_precalculados
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))   # permite ejecutar este archivo directamente
import json
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.transformers import ActiveSpaceTransformer
from qiskit_nature.second_q.mappers import JordanWignerMapper
from vqe.geometrias import MODELOS
from vqe.motor_vqe import ARCHIVO_PRECALCULADO, clave_caso

# Casos usados por los demos: geometrías de MODELOS con espacio activo (2, 2) y el H2 completo del intro
CASOS = [(geo, (2, 2)) for modelo in MODELOS.values() for geo, _ in modelo.values()]
CASOS.append(('H 0 0 0; H 0 0 0.735', None))


def generar():
    datos = {}
    for coordenadas, activo in CASOS:
        problem = PySCFDriver(atom=coordenadas, basis='sto3g', charge=0, spin=0).run()
        if activo is not None:
            problem = ActiveSpaceTransformer(num_electrons=activo[0], num_spatial_orbitals=activo[1]).transform(problem)
        op = JordanWignerMapper().map(problem.hamiltonian.second_q_op())
        datos[clave_caso(coordenadas, activo)] = {
            'orbitales': int(problem.num_spatial_orbitals),
            'particulas': [int(n) for n in problem.num_particles],
            'constante': float(sum(problem.hamiltonian.constants.values())),
            'paulis': op.paulis.to_labels(),
            'coeficientes': [[float(c.real), float(c.imag)] for c in op.coeffs],
        }
        print(f'[+] {coordenadas} | activo={activo}: {len(op)} términos')
    ARCHIVO_PRECALCULADO.write_text(json.dumps(datos, indent=1), encoding='utf-8')
    print(f'Guardado en {ARCHIVO_PRECALCULADO}')


if __name__ == '__main__':
    generar()
