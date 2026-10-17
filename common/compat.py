# common/compat.py - primitivas disponibles (V1 en Qiskit 1.x, V2 en Qiskit 2.x) y avisos silenciados
import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)

try:
    from qiskit.primitives import Sampler, Estimator
except ImportError:
    from qiskit.primitives import StatevectorSampler as Sampler
    from qiskit.primitives import StatevectorEstimator as Estimator

__all__ = ['Sampler', 'Estimator']
