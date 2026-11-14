import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(70)
box(ax, 2, 28, 24, 12, 'sujet', label=r'$\sqrt{8}\,\sqrt{48}$', size='m')
arrow(ax, (14, 41), (14, 56), 'fixe'); text(ax, 14, 62, 'multiplier d’abord', 'fixe', 's')
arrow(ax, (27, 56), (38, 56), 'fixe') if False else None
box(ax, 34, 52, 24, 10, 'fixe', label=r'$\sqrt{384}$', size='m', dash=True)
text(ax, 72, 57, 'grand nombre', 'fixe', 's')
arrow(ax, (14, 27), (14, 13), 'varie'); text(ax, 14, 6, 'simplifier d’abord', 'varie', 's')
box(ax, 34, 8, 30, 10, 'varie', label=r'$2\sqrt{2}\cdot4\sqrt{3}$', size='s')
arrow(ax, (65, 13), (70, 13), 'varie')
box(ax, 72, 8, 14, 10, 'resultat', label=r'$8\sqrt{6}$', size='s')
text(ax, 60, 22, 'petits nombres', 'resultat', 's')
save(fig, '22-094')
