import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Trois tests de symétrie : on remplace une coordonnée, puis on compare l'équation à l'ancienne
fig, ax = canvas(112)
text(ax, 44, 108, 'remplacer, puis comparer', 'encre', 'm')
rows = [(r'$\theta \rightarrow -\theta$', 'axe des $x$', 'x'),
        (r'$\theta \rightarrow \pi - \theta$', 'axe des $y$', 'y'),
        (r'$r \rightarrow -r$', 'le pôle $O$', 'o')]
for i, (sub, sym, kind) in enumerate(rows):
    y = 84 - 30 * i
    box(ax, 2, y - 6, 30, 12, 'varie', label=sub, size='s')
    arrow(ax, (33, y), (41, y), 'varie')
    c = (62, y)
    line(ax, [(c[0] - 14, c[1]), (c[0] + 14, c[1])], 'fixe', lw=0.7)
    line(ax, [(c[0], c[1] - 11), (c[0], c[1] + 11)], 'fixe', lw=0.7)
    p = (c[0] + 7, c[1] + 6)
    q = {'x': (c[0] + 7, c[1] - 6), 'y': (c[0] - 7, c[1] + 6), 'o': (c[0] - 7, c[1] - 6)}[kind]
    line(ax, [p, q], 'varie', lw=0.8, dash=True)
    disc(ax, p[0], p[1], 1.2, 'sujet'); disc(ax, q[0], q[1], 1.2, 'varie')
    text(ax, c[0], c[1] - 14, sym, 'varie', 's')
    if i == 0:
        text(ax, p[0] + 3.5, p[1] + 2.5, '$M$', 'sujet', 's')
        text(ax, q[0] + 8, q[1], 'image', 'varie', 's')
box(ax, 2, 0, 84, 8, 'resultat', label='même équation (équivalente) : la symétrie existe', size='s')
save(fig, '40-039')
