import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 39.5, 66, 'im', 'sujet', 14, ha='right', weight='bold'); text(ax, 39.5, 66, 'age', 'fixe', 14, ha='left')
line(ax, [(24, 60), (24, 58.5), (39.5, 58.5), (39.5, 60)], 'sujet')
text(ax, 31.7, 55, 'début du mot', 'sujet', 's')
box(ax, 2, 22, 24, 24, 'fixe', label='anneau\nde départ', size='s')
arrow(ax, (27, 34), (46, 34), 'varie', lw=1.4)
text(ax, 36.5, 38.5, r'$\eta$', 'varie', 'l')
box(ax, 47, 18, 39, 30, 'fixe')
text(ax, 66.5, 43, "anneau d’arrivée", 'fixe', 's')
for i in range(4):
    box(ax, 49.5 + i * 9, 22, 8, 10, 'resultat', label=str(i), size='m')
text(ax, 44, 8, r'im $\eta$ : image de $\eta$', 'resultat', 'm')
save(fig, '52-152')
