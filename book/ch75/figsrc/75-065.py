import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
y = 58
text(ax, 38, y, r'$U$', 'sujet', 20); text(ax, 45.5, y, r'$($', 'fixe', 20); text(ax, 52, y, r'$n$', 'varie', 20); text(ax, 58.5, y, r'$)$', 'fixe', 20)
box(ax, 4, 28, 38, 12, 'sujet', label='groupe unitaire')
box(ax, 46, 28, 38, 12, 'varie', label='coordonnées complexes')
arrow(ax, (38, 50), (23, 41.5), 'sujet'); arrow(ax, (52, 50), (65, 41.5), 'varie')
text(ax, 23, 45, 'la lettre', 'sujet', 's'); text(ax, 66, 45, 'le nombre', 'varie', 's')
box(ax, 8, 4, 72, 14, 'resultat', label=r'les $\eta$ qui gardent $H$')
arrow(ax, (23, 27), (23, 19.5), 'sujet'); arrow(ax, (65, 27), (65, 19.5), 'varie')
save(fig, '75-065')
