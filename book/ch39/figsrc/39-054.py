import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# la notation |z| : deux barres autour de la lettre z
fig, ax = canvas(66)
bx = [(24, 10, '|'), (36, 16, 'z'), (54, 10, '|')]
for x, w, s in bx:
    box(ax, x, 44, w, 12, 'sujet', label=s, size='l', weight='bold')
brace(ax, 24, 64, 58, 'sujet', label='distance de O au point z', down=False)
arrow(ax, (44, 44), (44, 35), 'fixe', lw=0.9)
text(ax, 44, 31, 'z : le nombre, ici 3 + 4i', 'fixe', 'm')
box(ax, 4, 11, 38, 10, 'resultat', label='|3 + 4i| = 5', size='m')
box(ax, 46, 11, 38, 10, 'autre', label='|−3| = 3 (réel)', size='m')
text(ax, 23, 5, 'module', 'resultat', 's')
text(ax, 65, 5, 'valeur absolue', 'autre', 's')
save(fig, '39-054')
