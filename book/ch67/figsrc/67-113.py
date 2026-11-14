import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(108)
Y = [14, 36, 58, 80, 102 - 2]
def tl(a, b, r=5.2):
    dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy); k = r / L
    line(ax, [(a[0] + dx * k, a[1] + dy * k), (b[0] - dx * k, b[1] - dy * k)], 'fixe', lw=1.0)
pos = {1: (44, Y[0]), 2: (24, Y[1]), 3: (64, Y[1]), 4: (24, Y[2]), 6: (64, Y[2]), 8: (24, Y[3]), 12: (64, Y[3]), 24: (44, Y[4])}
rl = {1: 'sujet', 2: 'varie', 3: 'varie', 4: 'resultat', 6: 'resultat', 8: 'autre', 12: 'autre', 24: 'sujet'}
for a, b in ((1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 8), (4, 12), (6, 12), (8, 24), (12, 24)):
    tl(pos[a], pos[b])
for d, (x, y) in pos.items(): disc(ax, x, y, 5.2, rl[d], label=str(d), size='m')
line(ax, [(30.5, Y[3]), (57.5, Y[3])], 'limite', dash=True)
text(ax, 44, Y[3] + 3.6, '×', 'limite', 'l'); text(ax, 44, Y[3] - 3.6, '8 ne divise pas 12', 'limite', 's')
text(ax, 44, 3, r'disque $d$ : sous-corps de $\mathbb{F}_{p^{24}}$', 'encre', 's')
save(fig, '67-113')
