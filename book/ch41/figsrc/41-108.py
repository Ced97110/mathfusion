import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(52)
box(ax, 4, 38, 34, 10, 'fixe', label=r'$3\times4=12$', size='l')
text(ax, 42, 43, 'fois : donne un nombre', 'fixe', 's', ha='left')
box(ax, 4, 22, 34, 10, 'sujet', label=r'$u\times v$', size='l')
text(ax, 42, 27, 'croix : donne un vecteur', 'sujet', 's', ha='left')
box(ax, 4, 4, 34, 10, 'autre', label=r'$u\wedge v$', size='l')
text(ax, 42, 9, 'même vecteur (français)', 'autre', 's', ha='left')
arrow(ax, (21, 21), (21, 15), 'varie', both=True)
text(ax, 25, 18, 'égaux', 'varie', 's', ha='left')
save(fig, '41-108')
