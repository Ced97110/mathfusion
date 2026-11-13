import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import itertools
fig, ax = canvas(64)
def shape(k, x, y, s=2.2):
    if k == 0: disc(ax, x, y, s, 'sujet')
    elif k == 1: box(ax, x - s, y - s, 2 * s, 2 * s, 'sujet', r=0.3)
    else: poly(ax, [(x - s, y - s), (x + s, y - s), (x, y + s)], 'sujet')
box(ax, 46, 6, 40, 54, 'fixe')
text(ax, 66, 54, r'$S_3$ : 6 ordres', 'sujet', 'm')
for n, p in enumerate(itertools.permutations(range(3))):
    c, r = n % 2, n // 2
    for j, k in enumerate(p): shape(k, 51 + c * 18 + j * 6.5, 42 - r * 12)
text(ax, 22, 50, r'$S_n$', 'sujet', 'xl')
arrow(ax, (34, 50), (45, 50), 'sujet')
text(ax, 22, 34, r'$S$ : tous les', 'sujet', 'm'); text(ax, 22, 29, 'réarrangements', 'sujet', 'm')
text(ax, 22, 18, r'$n$ : le nombre', 'varie', 'm'); text(ax, 22, 13, "d'objets", 'varie', 'm')
save(fig, '45-081')
