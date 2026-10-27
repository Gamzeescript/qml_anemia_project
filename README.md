<div align="center">

### ⚛️ Quantum Machine Learning - De Qubits a Moléculas ⚛️

<br><br>

---

> *"Si crees que entiendes la mecánica cuántica, es que no entiendes la mecánica cuántica."*  
> — **Richard Feynman**

</div>

<br><br>

<details id="#-visión-general-del-sistema">
<summary><b>🌌 Visión General</b></summary>

## 🌌 Visión General del Sistema

Bienvenido al nexo del proyecto. Este repositorio aborda un mismo problema clínico de salud —**la anemia**— a través de dos perspectivas complementarias de la computación cuántica en la era NISQ (dispositivos ruidosos de escala intermedia):

1. **Clasificación con Quantum Machine Learning (QML):** Un Clasificador Cuántico Variacional (VQC) que utiliza un `ZZFeatureMap` y un ansatz `RealAmplitudes` para procesar y clasificar variables clínicas del hemograma (como hemoglobina y volumen corpuscular medio).

2. **Simulación Cuántica Molecular:** Uso de VQE (Variational Quantum Eigensolver) para calcular energías del estado fundamental sobre espacios activos en moléculas de interés biológico (como el núcleo del hemo o la vitamina B12).

</details>

<details id="#-estructura-del-proyecto">
<summary><b>📐 Estructura del proyecto</b></summary>

El código está organizado por lo que se quiere mostrar: clasificación (QML), molécula (VQE) y modelo 3D.

```
qml_anemia_project/
├── README.md
├── main.py                      # menú interactivo para el live demo
├── verificar_entorno.py         # revisa Python, versiones, PySCF y el callback del VQC
├── requirements.txt             # dependencias (Windows, Mac y Linux)
├── requirements-vqe.txt         # opcional: agrega PySCF (Linux, macOS, WSL o Colab)
│
├── common/
│   └── compat.py                # elige las primitivas de Qiskit (V1 o V2) y silencia avisos
│
├── qml/                         # BLOQUE 1 · clasificación (demos 1 y 2)
│   ├── datos.py                 # datos sintéticos: anemia (Hb, VCM) y lunas
│   ├── modelo_vqc.py            # escalado, creación del VQC, callback y utilidades
│   ├── diagnostico_anemia.py    # DEMO 1: diagnóstico con VQC
│   ├── benchmark_vs_svm.py      # DEMO 2: VQC vs SVM (kernel RBF)
│   ├── convergencia_lunas.py    # extra: curva de convergencia de la pérdida
│   └── vqc_basico.py            # extra: VQC introductorio
│
├── vqe/                         # BLOQUE 2 · la molécula (demo 3)
│   ├── geometrias.py            # geometrías: Fe–O (charla) y H2 (plan B)
│   ├── motor_vqe.py             # integrales > Jordan-Wigner > UCCSD > VQE
│   ├── datos_precalculados.json # integrales precalculadas (modo sin PySCF)
│   ├── generar_precalculados.py # regenera ese archivo (requiere PySCF)
│   ├── vqe_h2_intro.py          # intro: VQE de H2
│   ├── comparacion_hemo.py      # DEMO 3: comparación de energías y ΔE
│   └── hemo_core_avanzado.py    # avanzado: núcleo del hemo (requiere PySCF)
│
├── visor_3d/                    # BLOQUE 3 · modelo 3D (demo 4)
│   ├── index.html               # visor molecular (3Dmol.js)
│   ├── estilo.css
│   ├── modelos.js               # estructuras PDB y estilos por anemia
│   ├── visor.js                 # lógica del visor
│   ├── servir.py                # servidor local (modo sin internet)
│   └── pdb/                     # coloca aquí 1GZX.pdb, 2HBS.pdb y 1BMT.pdb
│
└── diapositivas/
  └── dibujar_circuitos.py     # genera imágenes de los circuitos para las diapositivas

```
El extra de la estructura es el agregado de la presentación powerpoint

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
**R:** Es el mapeo más simple: un qubit por espín-orbital. Otros mapeos (Parity, Bravyi–Kitaev) pueden reducir la cantidad de qubits.

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


<details id="#-anexos">
<summary><b>📝 Anexos - notas </b></summary>


## Demos y su relación con la presentación

| Demo | Opción del menú | Qué muestra | Archivo |
|---|---|---|---|
| Demo 1 | 1 | Diagnóstico de anemia con VQC | `qml/diagnostico_anemia.py` |
| Demo 2 | 2 | VQC contra SVM, con matrices de confusión | `qml/benchmark_vs_svm.py` |
| Extra | 3 | Curva de convergencia de la pérdida | `qml/convergencia_lunas.py` |
| Extra | 4 | VQC básico | `qml/vqc_basico.py` |
| Intro | 5 | VQE de H₂ | `vqe/vqe_h2_intro.py` |
| Demo 3 | 6 | Energías de dos geometrías y ΔE | `vqe/comparacion_hemo.py` |
| Avanzado | 7 | Núcleo del hemo (8 qubits) | `vqe/hemo_core_avanzado.py` |
| Demo 4 | 8 | Visor molecular 3D | `visor_3d/index.html` |
| Recorrido | 9 | Encadena los demos 1, 2, 6 y 8 (solo para ensayar tiempos) | `main.py` |

## Requisitos

- Python 3.10 o superior (probado con 3.12).
- Versiones con las que se probó el proyecto:

| Paquete | Versión |
|---|---|
| qiskit | 2.5.2 |
| qiskit-machine-learning | 0.9.1 |
| qiskit-algorithms | 0.4.0 |
| qiskit-nature | 0.8.0 |
| scikit-learn | 1.8.0 |
| numpy | 2.4.4 |
| matplotlib | 3.10.8 |
| pyscf (opcional) | 2.14.0 |

- Para el visor 3D: un navegador e internet (descarga las estructuras de RCSB), o archivos PDB locales en `visor_3d/pdb/`.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Con Anaconda:

```bash
conda create -n qml python=3.12 -y
conda activate qml
pip install -r requirements.txt
```

**PySCF es opcional.** No tiene soporte nativo en Windows (por eso mismo se utilizó anaconda). Sin él, el VQE usa las integrales precalculadas de `vqe/datos_precalculados.json` para las geometrías de la charla (Fe–O y H₂) y da los mismos resultados. PySCF solo hace falta para calcular geometrías nuevas y para `hemo_core_avanzado.py`:

```bash
pip install -r requirements-vqe.txt   # Linux, macOS, WSL o Colab
```

Muestra qué Python usas, las versiones instaladas y si el callback del VQC se ejecuta («Callback ejecutado N veces: OK»).

## Cómo ejecutar

Siempre desde la carpeta raíz del proyecto (la que contiene `main.py`).

```bash
python main.py                                    # menú con todas las opciones
python -m qml.diagnostico_anemia                  # demo 1
python -m qml.diagnostico_anemia --mapa zz        # contraste con entrelazamiento
python -m qml.benchmark_vs_svm                    # demo 2
python -m qml.convergencia_lunas                  # curva de convergencia
python -m vqe.vqe_h2_intro                        # intro VQE
python -m vqe.comparacion_hemo                    # demo 3 (plan B: --modelo h2)
python visor_3d/servir.py                         # visor 3D en http://localhost:8000
python diapositivas/dibujar_circuitos.py          # imágenes de los circuitos
```

Las ventanas de gráficas (opciones 2 y 3) bloquean el menú hasta que las cierras.

## Resultados de referencia

Valores obtenidos en las pruebas; en tu equipo pueden variar un poco, sobre todo los del VQC.

| Prueba | Resultado |
|---|---|
| VQE de H₂ | −1.857275 Ha (electrónica) y −1.137306 Ha (total) |
| Demo 1, ZFeatureMap | 100 % en entrenamiento y en prueba; el paciente (Hb 8.5, VCM 110) sale macrocítico |
| Demo 1, ZZFeatureMap | ≈ 50 % (el entrelazamiento no aporta: solo el VCM separa las clases) |
| Demo 2 | SVM ≈ 96.7 % en ≈ 0.002 s; VQC entre 70 % y 90 % en ≈ 45 s |
| Demo 3, Fe–O | E(2.8 Å) ≈ −1321.9177 Ha, E(1.7 Å) ≈ −1322.4282 Ha, ΔE ≈ −0.5105 Ha |
| Núcleo del hemo | ≈ −1536.011 Ha con 8 qubits, ≈ 1 min (requiere PySCF) |

## Solución de problemas

| Problema | Solución |
|---|---|
| `Failed building wheel for pyscf` (Windows) | No hace falta PySCF: usa `pip install -r requirements.txt`. |
| `Falta instalar: qiskit_nature` | Instala en el entorno activo con `pip install -r requirements.txt` y comprueba con `python verificar_entorno.py` que usas el Python correcto. |
| La curva de convergencia sale vacía | Revisa en la salida la línea «Diagnóstico del callback»; asegúrate de no mezclar archivos de versiones distintas del proyecto. |
| `No module named 'qml'` | Ejecuta desde la carpeta raíz, con `python main.py` o `python -m ...`. |
| Avisos de `tkinter` al cerrar una gráfica | Son inofensivos; no afectan los resultados. |
| La opción 7 dice que requiere PySCF | Es esperable sin PySCF; instálalo en Linux, macOS, WSL o Colab. |


## Limitaciones

- Los datos de anemia son **sintéticos** y las clases están separadas solo por el VCM.
- Con hemoglobina y VCM no se distinguen la anemia ferropénica y la talasemia; el diagnóstico real usa más análisis.
- El modelo Fe–O es un modelo didáctico (dos átomos, base STO-3G, 2 electrones en 2 orbitales), no la hemoglobina real.
- No hay ventaja cuántica demostrada en estos problemas: la SVM clásica iguala o supera al VQC y es mucho más rápida.


## 🚀 Guía de Instalación y Configuración Paso a Paso (Linux)

Puedes elegir entre la instalación nativa con **`venv` / `pip`** (recomendada para la mayoría de distros de Linux) o mediante **Conda**.

### Opción A: Instalación Nativa en Linux (`venv` + `pip`)

#### 1. Instalar dependencias del sistema operativo
Abre la terminal de Linux (`Ctrl + Alt + T`) e instala las herramientas esenciales de compilación y headers de Python:
```bash
sudo apt update
sudo apt install -y python3-pip python3-venv python3-dev build-essential
```

#### 2. Clonar / Ubicarte en el directorio del proyecto
Navega hasta la carpeta local de tu repositorio:
```bash
cd ~/qml_anemia_project
```

#### 3. Crear el entorno virtual
Crea un entorno aislado llamado `qml_env`:
```bash
python3 -m venv qml_env
```

#### 4. Activar el entorno virtual
```bash
source qml_env/bin/activate
```
*(Verás la etiqueta `(qml_env)` al inicio de la línea de comandos).*

#### 5. Actualizar `pip` e instalar dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
> **Nota:** Si no utilizas `requirements.txt`, puedes instalar las librerías manualmente:
> ```bash
> pip install numpy scikit-learn pyscf qiskit qiskit-nature qiskit-machine-learning qiskit-algorithms
> ```

---

### Opción B: Instalación con Conda / Miniforge en Linux

Si prefieres usar Conda en Linux:

```bash
# 1. Crear entorno con Python 3.10
conda create -n qml_env python=3.10 -y

# 2. Activar entorno
conda activate qml_env

# 3. Instalar librerías
conda install -c conda-forge pyscf numpy scikit-learn qiskit -y
pip install qiskit-nature qiskit-machine-learning qiskit-algorithms
```

---

## ⚙️ Configuración en Visual Studio Code

Para vincular el entorno en VS Code y habilitar el autocompletado de Pylance:

1. Abre el proyecto en VS Code: `code .`
2. Presiona **`Ctrl + Shift + P`** para abrir la paleta de comandos.
3. Selecciona **`Python: Select Interpreter`**.
4. Selecciona la ruta de tu entorno:
   * **Para venv nativo:** `./qml_env/bin/python`
   * **Para Conda:** `~/miniconda3/envs/qml_env/bin/python` (o la ruta correspondiente).

---

## 🏃‍♂️ Ejecución del Proyecto

Con el entorno activo en tu terminal de Linux, ejecuta el punto de entrada principal:

```bash
python3 main.py
```

</details>


<details id="#-licencias">
<summary><b>📜 Licencia</b></summary>

- **Autora:** Gamzeescript · 
- **Repositorio:** `https://github.com/Gamzeescript/qml_anemia_project`
- **Link a la presentación** `https://docs.google.com/presentation/d/1OLdV3kSXvZwXKAxCm5XlZ1eXhMqsL1SH_WDZKmWwWto/edit?usp=sharing`
- **Licencia:** `Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.`
- Construido con [Qiskit](https://www.ibm.com/quantum/qiskit), Qiskit Machine Learning, Qiskit Nature, PySCF, scikit-learn y [3Dmol.js](https://3dmol.csb.pitt.edu/).

</details>

<br><br>

<p align="center">

<img width="250"  src="https://github.com/Gamzeescript/qml_anemia_project/blob/Maestro/aesthetic%20readme/schro.jpeg">

</p>
