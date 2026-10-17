import warnings
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from qiskit.circuit.library import ZZFeatureMap, EfficientSU2
from qiskit_algorithms.utils import algorithm_globals
from qiskit_machine_learning.algorithms import VQC

try:
    from qiskit.primitives import Sampler                          # Qiskit 1.x
except ImportError:
    from qiskit.primitives import StatevectorSampler as Sampler    # Qiskit 2.x

warnings.filterwarnings('ignore', category=DeprecationWarning)
algorithm_globals.random_seed = 42

RANGO = (0, np.pi / 2)  
MAX_ITER = 200


def elegir_cobyla():
    # VQC solo llama al callback si el optimizador es del tipo que su versión espera
    # (según la versión, el SciPyOptimizer de qiskit-machine-learning o el de qiskit-algorithms)
    try:
        from qiskit_machine_learning.algorithms.trainable_model import SciPyOptimizer as esperado
    except ImportError:
        esperado = None
    candidatos = []
    try:
        from qiskit_machine_learning.optimizers import COBYLA as cobyla_ml
        candidatos.append(cobyla_ml)
    except ImportError:
        pass
    try:
        from qiskit_algorithms.optimizers import COBYLA as cobyla_alg
        candidatos.append(cobyla_alg)
    except ImportError:
        pass
    for cobyla in candidatos:
        if esperado is None or issubclass(cobyla, esperado):
            return cobyla
    return candidatos[0]


COBYLA = elegir_cobyla()


class Registro:
    # El callback que se pasa a VQC: guarda la pérdida de cada iteración y cuenta las llamadas
    def __init__(self):
        self.perdidas = []
        self.por_respaldo = 0

    def __call__(self, pesos, valor):
        self.perdidas.append(float(valor))
        print(f'Iteración {len(self.perdidas)} - Pérdida: {valor:.4f}')


class COBYLAConRespaldo(COBYLA):
    # COBYLA que garantiza el callback: si la versión instalada no lo ejecuta por sí sola,
    # lo llamamos aquí; si ya lo ejecutó, no se duplica.
    def __init__(self, maxiter, registro):
        super().__init__(maxiter=maxiter)
        self._registro = registro

    def minimize(self, fun, x0, jac=None, bounds=None):
        registro = self._registro

        def objetivo(x):
            antes = len(registro.perdidas)
            valor = fun(x)
            if len(registro.perdidas) == antes:
                registro.por_respaldo += 1
                registro(x, valor)
            return valor

        return super().minimize(objetivo, x0, jac=jac, bounds=bounds)


def ejecutar_convergencia():
    # 1. Datos: dos lunas, no linealmente separables
    X, y = make_moons(n_samples=100, noise=0.15, random_state=42)
    X = MinMaxScaler(feature_range=RANGO).fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 2. Circuito: ZZFeatureMap (entrelazamiento) + ansatz EfficientSU2
    n = X_train.shape[1]
    feature_map = ZZFeatureMap(feature_dimension=n, reps=2, entanglement='linear')
    ansatz = EfficientSU2(num_qubits=n, reps=3, entanglement='linear')

    # 3. VQC con callback: se ejecuta en cada iteración del optimizador
    registro = Registro()
    vqc = VQC(sampler=Sampler(), feature_map=feature_map, ansatz=ansatz,
              optimizer=COBYLAConRespaldo(MAX_ITER, registro), callback=registro)

    print(f'Optimizador: {COBYLA.__module__}.{COBYLA.__name__}')
    print('--- Entrenando VQC sobre lunas ---')
    vqc.fit(X_train, y_train)
    print(f'Exactitud en entrenamiento: {vqc.score(X_train, y_train) * 100:.2f}%')
    print(f'Exactitud en prueba: {vqc.score(X_test, y_test) * 100:.2f}%')
    total = len(registro.perdidas)
    print(f'Diagnóstico del callback: {total} iteraciones registradas '
          f'({total - registro.por_respaldo} nativas, {registro.por_respaldo} por respaldo)')

    # 4. Curva de convergencia (siempre se muestra la ventana; si no hay datos, lo indica)
    fig, ax = plt.subplots(figsize=(8, 4))
    if registro.perdidas:
        ax.plot(range(1, total + 1), registro.perdidas, marker='o', markersize=3, color='purple', linewidth=1.5)
    else:
        ax.text(0.5, 0.5, 'Sin datos: el callback no se ejecutó', ha='center', va='center',
                transform=ax.transAxes, fontsize=14, color='red')
    ax.set_title('Curva de convergencia de la pérdida (VQC)')
    ax.set_xlabel('Iteración del optimizador clásico')
    ax.set_ylabel('Valor de la función de costo')
    ax.grid(True, linestyle='--', alpha=0.6)
    fig.tight_layout()
    fig.savefig('convergencia_lunas.png', dpi=150)   # copia para las diapositivas o como plan B
    print('Gráfica guardada en convergencia_lunas.png')
    plt.show()
    plt.close('all')


if __name__ == '__main__':
    ejecutar_convergencia()
