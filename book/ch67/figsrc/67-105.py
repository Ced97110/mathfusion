import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
def tl(a, b, r=5.2):
    dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy); k = r / L
    line(ax, [(a[0] + dx * k, a[1] + dy * k), (b[0] - dx * k, b[1] - dy * k)], 'fixe', lw=1.0)
pos = {1: (44, 18), 2: (24, 40), 3: (64, 40), 4: (24, 62), 6: (64, 62), 12: (44, 84)}
rl = {1: 'sujet', 2: 'varie', 3: 'varie', 4: 'resultat', 6: 'resultat', 12: 'sujet'}
for a, b in ((1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 12), (6, 12)):
    tl(pos[a], pos[b])
for d, (x, y) in pos.items(): disc(ax, x, y, 5.2, rl[d], label=str(d), size='m')
line(ax, [(30.5, 62), (57.5, 62)], 'limite', dash=True)
text(ax, 44, 65.5, '×', 'limite', 'l'); text(ax, 44, 57.5, 'aucun trait', 'limite', 's')
text(ax, 44, 4, r'disque $d$ : sous-corps à $p^d$ éléments', 'encre', 's')
save(fig, '67-105')
