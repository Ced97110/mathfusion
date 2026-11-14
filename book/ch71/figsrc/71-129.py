import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
box(ax, 4, 14, 24, 34, 'sujet', label=r'$V$', size='xl')
text(ax, 16, 53, 'ensemble de flèches', 'sujet', 's')
# plane
o = (46, 38)
arrow(ax, o, (60, 38), 'fixe'); arrow(ax, o, (46, 52), 'fixe')
arrow(ax, o, (58, 49), 'sujet', lw=1.4)
line(ax, [(58, 49), (58, 38)], 'varie', dash=True); line(ax, [(58, 49), (46, 49)], 'varie', dash=True)
text(ax, 72, 46, r'$n=2$', 'varie', 'l'); text(ax, 72, 40, 'plan', 'fixe', 's')
# space
o3 = (52, 12)
for a in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
    arrow(ax, o3, iso(*[v * 10 for v in a], origin=o3), 'fixe')
arrow(ax, o3, iso(8, 3, 6, origin=o3), 'sujet', lw=1.4)
text(ax, 72, 22, r'$n=3$', 'varie', 'l'); text(ax, 72, 16, 'espace', 'fixe', 's')
arrow(ax, (28, 38), (40, 42), 'fixe'); arrow(ax, (28, 24), (40, 20), 'fixe')
save(fig, '71-129')
