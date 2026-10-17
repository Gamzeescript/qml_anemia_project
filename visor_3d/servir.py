# visor_3d/servir.py - sirve el visor en http://localhost:8000 (permite usar archivos locales en pdb/)
import http.server
import os
import socketserver
import webbrowser
from pathlib import Path

PUERTO = 8000

if __name__ == '__main__':
    os.chdir(Path(__file__).parent)
    with socketserver.TCPServer(('', PUERTO), http.server.SimpleHTTPRequestHandler) as servidor:
        webbrowser.open(f'http://localhost:{PUERTO}/index.html')
        print(f'Visor en http://localhost:{PUERTO}/index.html (Ctrl+C para detener)')
        servidor.serve_forever()
