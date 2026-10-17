import importlib
import sys
import webbrowser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent


def correr(modulo, funcion, *args):
    # Importa el módulo al usarlo (el menú abre rápido) y ejecuta su función principal
    return lambda: getattr(importlib.import_module(modulo), funcion)(*args)


def comparacion_vqe():
    modelo = input('Modelo [fe_o / h2] (Enter = fe_o): ').strip() or 'fe_o'
    importlib.import_module('vqe.comparacion_hemo').ejecutar_simulacion_molecular(modelo)


def abrir_visor():
    webbrowser.open((RAIZ / 'visor_3d' / 'index.html').as_uri())


def pipeline_demos():
    for demo in ('1', '2', '6', '8'):
        SECCIONES_OPCIONES[demo][1]()


BLOQUES = [
    ('BLOQUE 1 · QML: clasificación (Demos 1 y 2)', {
        '1': ('DEMO 1 · Diagnóstico de anemia con VQC', correr('qml.diagnostico_anemia', 'ejecutar_diagnostico_qml')),
        '2': ('DEMO 2 · Benchmark VQC vs SVM (RBF)', correr('qml.benchmark_vs_svm', 'ejecutar_benchmark')),
        '3': ('Extra · Curva de convergencia (lunas)', correr('qml.convergencia_lunas', 'ejecutar_convergencia')),
        '4': ('Extra · VQC básico (make_blobs)', correr('qml.vqc_basico', 'ejecutar_vqc_basico')),
    }),
    ('BLOQUE 2 · VQE: la molécula (Demo 3)', {
        '5': ('Intro · VQE de H2', correr('vqe.vqe_h2_intro', 'simular_h2')),
        '6': ('DEMO 3 · Comparación de energías y ΔE', comparacion_vqe),
        '7': ('Avanzado · Núcleo del hemo (puede tardar)', correr('vqe.hemo_core_avanzado', 'evaluar_nucleo_hemo')),
    }),
    ('BLOQUE 3 · Modelo 3D (Demo 4)', {
        '8': ('DEMO 4 · Abrir visor molecular 3D', abrir_visor),
    }),
]

SECCIONES_OPCIONES = {}
for _, opciones in BLOQUES:
    SECCIONES_OPCIONES.update(opciones)
SECCIONES_OPCIONES['9'] = ('Recorrido completo (Demos 1 a 4)', pipeline_demos)


def menu():
    while True:
        print()
        print('#' * 60)
        print(' PROYECTO QML: DIAGNÓSTICO Y SIMULACIÓN MOLECULAR DE ANEMIA')
        print('#' * 60)
        for titulo, opciones in BLOQUES:
            print(f'\n{titulo}')
            for clave, (nombre, _) in opciones.items():
                print(f'  {clave}. {nombre}')
        print('\n  9. Recorrido completo (Demos 1 a 4)')
        print('  0. Salir')
        opcion = input('\nSelecciona una opción: ').strip()
        if opcion == '0':
            print('Cerrando...')
            sys.exit()
        if opcion in SECCIONES_OPCIONES:
            try:
                SECCIONES_OPCIONES[opcion][1]()
            except ModuleNotFoundError as error:
                print(f'[!] Falta instalar: {error.name}. Ejecuta: pip install -r requirements.txt')
            except Exception as error:   # no cortar el live demo si algo falla
                print(f'[!] Error: {error}')
        else:
            print('Opción inválida. Intenta de nuevo.')


if __name__ == '__main__':
    menu()
