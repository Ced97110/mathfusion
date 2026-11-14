import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(66)
box(ax, 2, 46, 22, 12, 'fixe', label=r'$2\pi$', size='l')
box(ax, 33, 46, 22, 12, 'fixe', label=r'$\div\ 360$', size='m')
box(ax, 62, 46, 24, 12, 'varie', label='0,01745', size='m')
arrow(ax, (24, 52), (33, 52), 'fixe')
arrow(ax, (55, 52), (62, 52), 'fixe')
text(ax, 13, 63, '≈ 6,2832', 'fixe', 's')
text(ax, 71, 34, 'troisième nombre', 'varie', 's', ha='right')
box(ax, 4, 8, 22, 14, 'sujet', label='500', size='l')
box(ax, 33, 8, 22, 14, 'autre', label='12', size='l')
box(ax, 62, 8, 24, 14, 'varie', label='0,01745', size='m')
arrow(ax, (74, 44), (74, 25), 'varie')
text(ax, 15, 28, 'rayon', 'sujet', 's')
text(ax, 44, 28, 'angle', 'autre', 's')
save(fig, '29-005')
