# vqe/geometrias.py - geometrías moleculares (en Å) usadas en los demos de VQE
# 'fe_o' es el modelo de la charla; 'h2' es el plan B (ejemplo estándar de Qiskit Nature)
MODELOS = {
    'fe_o': {
        'defectuoso': ('Fe 0.0 0.0 0.0; O 0.0 0.0 2.8', 'Hemo defectuoso (enlace Fe-O 2.8 Å)'),
        'sintetico': ('Fe 0.0 0.0 0.0; O 0.0 0.0 1.7', 'Molécula sintética (enlace Fe-O 1.7 Å)'),
    },
    'h2': {
        'defectuoso': ('H 0.0 0.0 0.0; H 0.0 0.0 2.0', 'H2 estirado (2.0 Å)'),
        'sintetico': ('H 0.0 0.0 0.0; H 0.0 0.0 0.735', 'H2 en equilibrio (0.735 Å)'),
    },
}

# Núcleo del hemo (modelo reducido, sin anillo de porfirina): Fe, 4 N y un O
HEMO_CORE_XYZ = '; '.join([
    'Fe 0.0000 0.0000 0.0000',
    'N 1.9800 0.0000 0.0000',
    'N -1.9800 0.0000 0.0000',
    'N 0.0000 1.9800 0.0000',
    'N 0.0000 -1.9800 0.0000',
    'O 0.0000 0.0000 1.8000',
])
