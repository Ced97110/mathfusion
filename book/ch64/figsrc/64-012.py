import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 2, 58, 38, 12, 'sujet', label='résoluble par radicaux', size='s')
arrow(ax, (40.4, 64), (47.6, 64), 'encre', both=True)
text(ax, 44, 55.3, 'si et seulement si', 'encre', 's')
box(ax, 48, 58, 38, 12, 'autre', label='groupe de Galois résoluble', size='s')
text(ax, 44, 49, 'cas du degré 2 : deux solutions', 'fixe', 's')
for cx, role, lab, cross in ((22, 'fixe', 'ne rien échanger', False), (66, 'varie', 'échanger les deux', True)):
    disc(ax, cx - 6, 42, 3.3, 'sujet', label=r'$x_1$', size='s')
    disc(ax, cx + 6, 42, 3.3, 'sujet', label=r'$x_2$', size='s')
    disc(ax, cx - 6, 26, 3.3, 'sujet')
    disc(ax, cx + 6, 26, 3.3, 'sujet')
    if cross:
        arrow(ax, (cx - 5, 38.8), (cx + 5, 29.2), role)
        arrow(ax, (cx + 5, 38.8), (cx - 5, 29.2), role)
    else:
        arrow(ax, (cx - 6, 38.6), (cx - 6, 29.4), role)
        arrow(ax, (cx + 6, 38.6), (cx + 6, 29.4), role)
    text(ax, cx, 19, lab, role, 's')
text(ax, 44, 11, 'groupe de Galois : 2 éléments', 'autre', 's')
text(ax, 44, 5, 'solution en 1 étage : racine carrée', 'sujet', 's')
save(fig, '64-012')
