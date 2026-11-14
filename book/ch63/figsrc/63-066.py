import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# ligne 1 : conjugués, le remplacement existe
text(ax, 44, 70, r'$\sqrt{2}$ et $-\sqrt{2}$ : conjugués', 'resultat', 'm')
box(ax, 2, 46, 22, 14, 'sujet', label=r'$\sqrt{2}$')
box(ax, 40, 46, 22, 14, 'autre', label=r'$-\sqrt{2}$')
arrow(ax, (24.5, 53), (39.5, 53), 'varie')
text(ax, 32, 57.5, r'$\varphi$', 'varie', 'm')
box(ax, 66, 46, 20, 14, 'resultat', label=r'$2\mapsto2$', size='s')
# ligne 2 : non conjugués, contradiction
text(ax, 44, 36, r'$\sqrt{2}$ et $\sqrt{3}$ : pas conjugués', 'limite', 'm')
box(ax, 2, 12, 22, 14, 'sujet', label=r'$\sqrt{2}$')
box(ax, 40, 12, 22, 14, 'autre', label=r'$\sqrt{3}$')
arrow(ax, (24.5, 19), (39.5, 19), 'varie')
text(ax, 32, 23.5, r'$\varphi$', 'varie', 'm')
box(ax, 66, 12, 20, 14, 'limite', label=r'$2\mapsto3$', size='s')
text(ax, 44, 5, r'$\varphi$ doit fixer 2 : $3\neq2$', 'limite', 's')
save(fig, '63-066')
