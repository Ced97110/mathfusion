import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 4, 58, 'files de 4 élèves', 'sujet', 's', ha='left')
for i, t in enumerate([r'$\mathbb{Z}/2$', r'$\mathbb{Z}/3$', r'$\mathbb{Z}/2$', r'$\mathbb{Z}/2$']):
    box(ax, 4 + i * 15, 44, 13, 9, 'resultat', label=t)
text(ax, 66, 48.5, 'résoluble', 'resultat', 'm', ha='left', weight='bold')
text(ax, 4, 40, 'tous premiers', 'resultat', 's', ha='left')
text(ax, 4, 34, 'files paires de 5', 'sujet', 's', ha='left')
box(ax, 4, 20, 58, 9, 'limite', label='un seul facteur : 60')
text(ax, 66, 24.5, 'non résoluble', 'limite', 'm', ha='left', weight='bold')
text(ax, 4, 14, 'ce 60 n’est pas premier', 'limite', 's', ha='left')
text(ax, 44, 4, r'résoluble $\Leftrightarrow$ tous premiers', 'encre', 's')
save(fig, '64-083')
