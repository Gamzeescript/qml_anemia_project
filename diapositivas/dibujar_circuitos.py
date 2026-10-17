# diapositivas/dibujar_circuitos.py - genera imágenes de los circuitos para las diapositivas 6 y 7
from pathlib import Path
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes

carpeta = Path(__file__).parent
feature_map = ZZFeatureMap(feature_dimension=2, reps=2, entanglement='full')
ansatz = RealAmplitudes(num_qubits=2, reps=2, entanglement='linear')

feature_map.decompose().draw('mpl', filename=str(carpeta / 'circuito_feature_map.png'))
ansatz.decompose().draw('mpl', filename=str(carpeta / 'circuito_ansatz.png'))
print('Imágenes generadas en la carpeta diapositivas/')
