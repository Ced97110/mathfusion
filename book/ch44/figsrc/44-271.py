import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def square(cx, cy, labs, role):
    a = 9.0
    box(ax, cx - a, cy - a, 2 * a, 2 * a, role, r=0.5)
    for (dx, dy), l in zip([(-a, -a), (a, -a), (a, a), (-a, a)], labs):
        disc(ax, cx + dx, cy + dy, 3.0, 'sujet', label=l, size='s')
square(20, 24, ['1', '2', '3', '4'], 'fixe')
square(68, 24, ['4', '1', '2', '3'], 'fixe')
arrow(ax, (33, 24), (55, 24), 'varie', lw=1.2)
text(ax, 44, 29, 'quart de tour', 'varie', 's')
text(ax, 20, 44, 'coins de départ', 'encre', 's')
text(ax, 68, 44, 'coins après', 'encre', 's')
text(ax, 44, 4, 'un mouvement envoie chaque coin sur un coin', 'encre', 's')
save(fig, '44-271')
