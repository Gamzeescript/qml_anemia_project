<div align="center">

# ⚛️ `PROJECT::QUANTUM_CORE` ⚛️

### *Superponiendo posibilidades, colapsando soluciones.*

<p align="center">
  <img src="https://img.shields.io/badge/State-|Ψ⟩_Superposition-8A2BE2?style=for-the-badge&logo=quantum&logoColor=white" alt="Quantum State">
  <img src="https://img.shields.io/badge/Entanglement-Active-00FFFF?style=for-the-badge&logo=atom&logoColor=black" alt="Entanglement">
  <img src="https://img.shields.io/badge/Qubits-1024_Active-FF007F?style=for-the-badge" alt="Qubits">
</p>

---

> *"Si crees que entiendes la mecánica cuántica, es que no entiendes la mecánica cuántica."*  
> — **Richard Feynman**

<br/>

<!-- 🧭 MENÚ DE NAVEGACIÓN RÁPIDA (ENLACES INTERNOS) -->
| [🌌 Visión General](#-visión-general-del-sistema) | [🚀 Instalación](#-sección-01-instalación-del-multiverso) | [❓ FAQ](#-sección-02-preguntas-frecuentes-faq) | [📖 Glosario](#-sección-03-glosario-cuántico) |
| :---: | :---: | :---: | :---: |

</div>

<br/>

## 🌌 Visión General del Sistema

Bienvenido al nexo del proyecto. Este repositorio aborda un mismo problema clínico de salud —**la anemia**— a través de dos perspectivas complementarias de la computación cuántica en la era NISQ (dispositivos ruidosos de escala intermedia)[cite: 1, 2]:

1. **Clasificación con Quantum Machine Learning (QML):** Un Clasificador Cuántico Variacional (VQC) que utiliza un `ZZFeatureMap` y un ansatz `RealAmplitudes` para procesar y clasificar variables clínicas del hemograma (como hemoglobina y volumen corpuscular medio)[cite: 1, 2].
2. **Simulación Cuántica Molecular:** Uso de VQE (Variational Quantum Eigensolver) para calcular energías del estado fundamental sobre espacios activos en moléculas de interés biológico (como el núcleo del hemo o la vitamina B12)[cite: 1].

<details id="#-sección-02-preguntas-frecuentes-faq">
<summary><b>❓ SECCIÓN 02: Preguntas Frecuentes (FAQ)</b></summary>
<br/>

### 💡 Dudas Comunes sobre el Núcleo Cuántico

#### Q: ¿Hay ventaja cuántica en estos demos?
**R:** No. Son problemas pequeños; una SVM clásica iguala o supera al VQC y es mucho más rápida. La ventaja cuántica en aprendizaje automático sigue siendo un tema de investigación abierto. El valor aquí es aprender la arquitectura[cite: 35].

#### Q: ¿Se cura la anemia con esto?
**R:** No. El VQE calcula energías; sirve para priorizar candidatos moleculares *in silico*, y después hace falta síntesis, pruebas de laboratorio y ensayos clínicos[cite: 35].

#### Q: ¿Por qué 2 qubits y por qué full y linear dan lo mismo?
**R:** Se usa un qubit por característica (Hb y VCM). Con 2 qubits solo existe un par de qubits que entrelazar, así que ambos patrones coinciden; la diferencia aparece con 3 o más[cite: 35].

#### Q: ¿Cómo paso a las cuatro anemias a la vez?
**R:** Pasa a multiclase: etiquetas con 4 clases (el VQC admite más de dos clases) y más variables clínicas (ferritina, RDW, recuento de glóbulos rojos, entre otras), un qubit por variable. Con datos reales y validación clínica; con solo Hb y VCM no se pueden separar ferropénica y talasemia[cite: 35].

#### Q: ¿Qué significa $\Delta E < 0$ y por qué energía total?
**R:** Energía total más baja = configuración más estable. Se usa la total porque la repulsión nuclear cambia con la distancia; compararla solo en la parte electrónica sería engañoso[cite: 35].

#### Q: ¿Necesito la nube?
**R:** Para estos demos no: corren en tu CPU y RAM con simuladores de Qiskit. Si prefieres no instalar nada, usa Google Colab. Para hardware real de IBM necesitas `qiskit-ibm-runtime`, un token de API y adaptar el código a las primitivas del backend; habrá colas y ruido. La memoria del simulador de vector de estado solo se vuelve crítica hacia ~28–32 qubits[cite: 35].

#### Q: ¿Por qué COBYLA y SLSQP?
**R:** COBYLA no necesita gradientes y tolera el ruido de muestreo, por eso se usa en el VQC. SLSQP usa gradientes y funciona bien en el VQE con simulación exacta (sin ruido)[cite: 35].

#### Q: ¿Por qué Jordan–Wigner?
**R:** Es el mapeo más simple: un qubit por espín-orbital. Otros mapeos (Parity, Bravyi–Kitaev) pueden reducir la cantidad de qubits[cite: 35].

</details>


<details id="#-sección-03-glosario-cuántico">
<summary><b>❓ SECCIÓN 03: Glosario</b></summary>


<br/>
</details>