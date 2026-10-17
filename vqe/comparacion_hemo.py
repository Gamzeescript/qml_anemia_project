# vqe/comparacion_hemo.py - DEMO 3: comparación de energías con VQE y cálculo de ΔE
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))   # permite ejecutar este archivo directamente
import argparse
from vqe.geometrias import MODELOS
from vqe.motor_vqe import energia_de_geometria


def calcular_energia(coordenadas, etiqueta):
    print(f'[+] Evaluando configuración: {etiqueta}...')
    _, _, e_total = energia_de_geometria(coordenadas, espacio_activo=(2, 2), charge=0, spin=0)
    print(f'    Energía total del estado fundamental: {e_total:.4f} Hartree')
    return e_total


def ejecutar_simulacion_molecular(modelo='fe_o'):
    print('=' * 50)
    print(' DEMO 3: SIMULACIÓN MOLECULAR Y COMPARACIÓN (VQE)')
    print('=' * 50)
    geo_def, etiqueta_def = MODELOS[modelo]['defectuoso']
    geo_sin, etiqueta_sin = MODELOS[modelo]['sintetico']

    e_def = calcular_energia(geo_def, etiqueta_def)
    e_sin = calcular_energia(geo_sin, etiqueta_sin)
    delta_e = e_sin - e_def

    print('=== Resultados de la comparación ===')
    print(f'E (defectuoso): {e_def:.4f} Hartree')
    print(f'E (sintético):  {e_sin:.4f} Hartree')
    print('-' * 45)
    print(f'Diferencia de estabilidad (ΔE = E_sintético - E_defectuoso): {delta_e:.4f} Hartree')
    if delta_e < 0:
        print('[OK] La configuración sintética tiene energía total más baja:')
        print('     es más estable en este modelo didáctico.')
    else:
        print('[!] La configuración sintética no resulta más estable en este modelo.')
        print('    Revisa la geometría o prueba con --modelo h2.')
    print('Nota: modelo didáctico; no representa una molécula terapéutica real.')
    return delta_e


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--modelo', choices=list(MODELOS), default='fe_o')
    ejecutar_simulacion_molecular(parser.parse_args().modelo)
