// visor.js - lógica del visor. Usa archivos locales en pdb/ si existen (servidor local); si no, descarga de RCSB
const viewer = $3Dmol.createViewer('visor-3d', { backgroundColor: '#2d2d2d' });
const texto = document.getElementById('texto-descripcion');
const btnBeta = document.getElementById('btn-beta');

function mostrar(m) {
  viewer.clear();
  const terminar = function () { m.estilo(viewer); viewer.zoomTo(); viewer.render(); };
  fetch('pdb/' + m.pdb + '.pdb')
    .then(function (r) { return r.ok ? r.text() : Promise.reject(); })
    .then(function (pdb) { viewer.addModel(pdb, 'pdb'); terminar(); })
    .catch(function () { $3Dmol.download('pdb:' + m.pdb, viewer, {}, terminar); });
}

function cargarModelo(tipo) {
  const m = modelos[tipo];
  mostrar(m);
  texto.innerHTML = m.texto;
  btnBeta.style.display = (tipo === 'talasemia') ? 'inline-block' : 'none';
}

document.querySelectorAll('button[data-modelo]').forEach(function (b) {
  b.addEventListener('click', function () { cargarModelo(b.dataset.modelo); });
});

btnBeta.addEventListener('click', function () {
  viewer.setStyle({ chain: ['B', 'D'] }, { cartoon: { color: '#2ecc71', opacity: 0.05 } });
  viewer.render();
});
