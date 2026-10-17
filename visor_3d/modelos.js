// modelos.js - qué estructura (PDB) se carga por anemia y cómo se resalta. Verifica los IDs en rcsb.org
const modelos = {
  ferropenica: {
    pdb: '1GZX',   // oxihemoglobina humana
    estilo: function (viewer) {
      viewer.setStyle({}, { cartoon: { color: 'white', opacity: 0.35 } });
      viewer.setStyle({ resn: 'HEM' }, { stick: { colorscheme: 'cyanCarbon' } });
      viewer.addStyle({ elem: 'Fe' }, { sphere: { color: 'red', radius: 1.5 } });
    },
    texto: '<b>Anemia ferropénica:</b> la esfera roja es el átomo de hierro en el centro del grupo hemo, donde se une el O₂. En esta anemia falta hierro disponible para formar hemo; aquí es una metáfora visual del sitio de unión. El hemo en sí no es defectuoso.'
  },
  falciforme: {
    pdb: '2HBS',   // hemoglobina falciforme (desoxi)
    estilo: function (viewer) {
      viewer.setStyle({}, { cartoon: { color: 'spectrum' } });
      // Posición 6 de las cadenas beta (suelen ser B y D; verifícalo en el PDB)
      viewer.addStyle({ chain: ['B', 'D'], resi: 6 }, { sphere: { color: 'magenta', radius: 1.2 } });
    },
    texto: '<b>Anemia falciforme:</b> las esferas magenta marcan la posición 6 de las cadenas β, donde un ácido glutámico es reemplazado por valina (Glu6Val). La valina crea un parche hidrofóbico que favorece que las moléculas de hemoglobina se peguen entre sí.'
  },
  talasemia: {
    pdb: '1GZX',
    estilo: function (viewer) {
      viewer.setStyle({ chain: ['A', 'C'] }, { cartoon: { color: '#4a90e2' } });
      viewer.setStyle({ chain: ['B', 'D'] }, { cartoon: { color: '#2ecc71' } });
      viewer.addStyle({ resn: 'HEM' }, { stick: { colorscheme: 'orangeCarbon' } });
    },
    texto: '<b>Talasemia:</b> cadenas α en azul y β en verde. Usa el botón Quitar cadenas β para simular una β-talasemia: las cadenas α quedan aisladas e inestables. Es una ilustración didáctica de un defecto de producción de cadenas.'
  },
  megaloblastica: {
    pdb: '1BMT',  // dominio de unión a B12 de la metionina sintasa
    estilo: function (viewer) {
      viewer.setStyle({}, { cartoon: { color: 'lightgray', opacity: 0.5 } });
      viewer.setStyle({ hetflag: true }, { stick: { colorscheme: 'greenCarbon' } });
      viewer.addStyle({ elem: 'Co' }, { sphere: { color: 'orange', radius: 1.8 } });
    },
    texto: '<b>Anemia megaloblástica:</b> dominio de unión a B12 de la metionina sintasa. La esfera naranja es el átomo de cobalto en el centro de la cobalamina. Esta anemia se debe al déficit de B12 o folato, que altera la síntesis de ADN.'
  }
};
