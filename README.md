<div align="center">

### ⚛️ Quantum Machine Learning - De Qubits a Moléculas ⚛️

---

> *"Si crees que entiendes la mecánica cuántica, es que no entiendes la mecánica cuántica."*  
> — **Richard Feynman**

</div>


<details id="#-visión-general-del-sistema">
<summary><b>🌌 Visión General</b></summary>

## 🌌 Visión General del Sistema

Bienvenido al nexo del proyecto. Este repositorio aborda un mismo problema clínico de salud —**la anemia**— a través de dos perspectivas complementarias de la computación cuántica en la era NISQ (dispositivos ruidosos de escala intermedia):

1. **Clasificación con Quantum Machine Learning (QML):** Un Clasificador Cuántico Variacional (VQC) que utiliza un `ZZFeatureMap` y un ansatz `RealAmplitudes` para procesar y clasificar variables clínicas del hemograma (como hemoglobina y volumen corpuscular medio).

2. **Simulación Cuántica Molecular:** Uso de VQE (Variational Quantum Eigensolver) para calcular energías del estado fundamental sobre espacios activos en moléculas de interés biológico (como el núcleo del hemo o la vitamina B12).

</details>

<details id="#-estructura-del-proyecto">
<summary><b>📐 Estructura del proyecto</b></summary>

</details>

<details id="#-estructura-del-proyecto">
<summary><b>📐 Estructura del proyecto</b></summary>

</details>

<details id="#-instalacion-del-proyecto">
<summary><b>🚀 Instalación del proyecto</b></summary>

Sigue estos comandos desde tu terminal para configurar de forma limpia todo el ecosistema de desarrollo:

### 1. Abrir el entorno de comandos
Abre la aplicación **Anaconda Prompt** desde el menú de inicio de tu computadora y navega hasta la ruta local de tu repositorio:
```bash
cd C:\Users\nombreusuario\Documents\GitHub\qml_anemia_project
```

### 2. Crear un entorno virtual limpio
Crea un entorno aislado utilizando una versión estable de Python (recomendado **Python 3.10** para compatibilidad óptima con Qiskit Nature):
```bash
conda create -n qml_env python=3.10 -y
```

### 3. Activar el entorno virtual
Activa el entorno para que todas las instalaciones posteriores operen dentro de este espacio aislado:
```bash
conda activate qml_env
```
*(Sabrás que está activo porque el indicador de la terminal cambiará a `(qml_env)`)*.

### 4. Instalar dependencias base y binarios (vía Conda)
Instala los componentes pesados y binarios que requieren compilación en C utilizando el canal oficial `conda-forge`:
```bash
conda install -c conda-forge pyscf numpy scikit-learn qiskit -y
```

### 5. Instalar librerías cuánticas especializadas (vía `pip`)
Completa la instalación del stack cuántico ejecutando:
```bash
pip install qiskit-nature qiskit-machine-learning qiskit-algorithms
```
*(Alternativamente, si prefieres usar el archivo de requerimientos del proyecto, puedes ejecutar: `pip install -r requirements.txt`)*.

---

## ⚙️ Configuración en Visual Studio Code

Para vincular el entorno en VS Code y eliminar cualquier advertencia de Pylance:
1. Abre la carpeta del proyecto en **VS Code**.
2. Presiona **`Ctrl + Shift + P`** para abrir la paleta de comandos.
3. Escribe y selecciona: **`Python: Select Interpreter`**.
4. Elige la ruta correspondiente al entorno creado: **`Python 3.10.22 (qml_env)`**.

---

## 🏃‍♂️ Ejecución del Proyecto

Abre una nueva terminal integrada dentro de VS Code (`Terminal > New Terminal`), verifica que aparezca `(qml_env)` al inicio de la línea y arranca el menú interactivo principal:
```bash
python main.py
```

---

Para esta parte si hay dudas, porfavor contactar al developer

## 🌐 Visor Molecular 3D Interactivo

Para visualizar las estructuras tridimensionales de las moléculas (control sano y tipos de anemia):
1. Abre el archivo `simulador_molecular.html` en cualquier navegador web moderno (Chrome, Edge, Firefox).
2. Utiliza los botones interactivos para alternar entre el modelo sano (control) y las patologías representadas.

</details>



<details id="#-requisitos-del-sistema">
<summary><b>🛠️ Requisitos del sistema</b></summary>

Antes de comenzar, asegúrate de contar con lo siguiente en tu equipo (entorno Windows):
* **[Anaconda](https://www.anaconda.com/) o [Miniforge](https://github.com/conda-forge/miniforge):** Esencial para gestionar entornos virtuales y evitar errores de compilación con las librerías de C/C++ (como PySCF).
* **[Visual Studio Code (VS Code)](https://code.visualstudio.com/):** Entorno de desarrollo recomendado, con las extensiones de **Python** y **Pylance** instaladas.

</details>


<details id="#-sección-02-preguntas-frecuentes-faq">
<summary><b>❓ FAQ</b></summary>
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
<summary><b>📖 Glosario</b></summary>

**Qubit**: unidad de información cuántica; puede estar en superposición de 0 y 1.
Entrelazamiento: correlación cuántica entre qubits que no se describe qubit por qubit;
aquí lo crean las compuertas CX/ZZ.

**Espacio de Hilbert**: el espacio matemático donde viven los estados de n qubits
(dimensión 2ⁿ).

**Feature map (ZZFeatureMap)**: circuito que codifica datos clásicos en un estado
cuántico.

**Ansatz (RealAmplitudes, UCCSD)**: circuito con parámetros ajustables; es el «modelo»
que se entrena.

**VQC - clasificador cuántico variacional**: feature map + ansatz + medición + optimizador
clásico.

**VQE -  algoritmo variacional que busca la energía mínima de un Hamiltoniano**:
Hamiltoniano operador que describe la energía del sistema (aquí, de los electrones de
la molécula).

**Estado fundamental (E₀)**: el estado de menor energía; el más estable.

**Hartree-Fock**: aproximación inicial de campo medio; punto de partida del VQE.

**UCCSD**: ansatz de excitaciones simples y dobles que captura correlación electrónica.

**Jordan–Wigner**: transformación que convierte operadores de electrones en
operadores de Pauli sobre qubits.

**Espacio activo**: subconjunto de electrones y orbitales que sí se simulan; el resto se
trata de forma aproximada.

**Sampler / Estimator - primitivas de Qiskit**: la primera entrega probabilidades de
medición; la segunda, valores esperados de observables.

**COBYLA / SLSQP**: optimizadores clásicos; COBYLA no usa gradientes y SLSQP sí (por
diferencias finitas en este caso).

**NISQ**: era de dispositivos cuánticos con ruido y pocos qubits

<br/>
</details>