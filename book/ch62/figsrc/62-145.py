import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
# deux cas côte à côte : l'hypothèse tient / l'hypothèse manque
box(ax, 2, 56, 40, 24, 'resultat', label='caractéristique 0\nou corps fini', size='s')
box(ax, 46, 56, 40, 24, 'limite', label=r'$(\mathbb{Z}/p\mathbb{Z})(t)$' + '\nni l’un ni l’autre', size='s')
arrow(ax, (22, 56), (22, 44), 'resultat', lw=1.2)
arrow(ax, (66, 56), (66, 44), 'limite', lw=1.2)
box(ax, 2, 28, 40, 16, 'resultat', label='irréductible :\nracines distinctes', size='s')
box(ax, 46, 28, 40, 16, 'limite', label=r'$x^p-t$ irréductible :' + '\nune racine répétée', size='s')
arrow(ax, (22, 28), (22, 18), 'resultat', lw=1.2)
arrow(ax, (66, 28), (66, 18), 'limite', lw=1.2)
box(ax, 2, 4, 40, 14, 'resultat', label='critère de\nséparabilité vrai', size='s')
box(ax, 46, 4, 40, 14, 'limite', label='critère de\nséparabilité faux', size='s')
save(fig, '62-145')
