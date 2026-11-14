import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
pw, gap = 26.0, 3.0
xs = [2 + i * (pw + gap) for i in range(3)]
titles = ['1. les racines', '2. permutations', '3. le sous-groupe']
roles = ['sujet', 'varie', 'resultat']
for x, t, r in zip(xs, titles, roles):
    box(ax, x, 4, pw, 62, role=r, fill=True)
    text(ax, x + pw / 2, 61, t, r, 's', weight='bold')

def tri(cx, cy, s=9):
    return [(cx + s, cy), (cx - s * 0.5, cy + s * 0.87), (cx - s * 0.5, cy - s * 0.87)]

CY = 36
for i in range(2):
    cx = xs[i] + pw / 2
    P = tri(cx + 1.5, CY, 8)
    poly(ax, P, 'fixe', fill=False, lw=0.6)
    for k, (px, py) in enumerate(P):
        disc(ax, px, py, 3.0, 'sujet', label=r'$r_%d$' % (k + 1), size='s')
# step 2 : the swap of r2 and r3, then the circuits r1 -> r2 -> r3 -> r1
P = tri(xs[1] + pw / 2 + 1.5, CY, 8)
(x1, y1), (x2, y2), (x3, y3) = P
arrow(ax, (x2 - 4.2, y2 - 1.2), (x3 - 4.2, y3 + 1.2), 'varie', lw=1.0, both=True)
text(ax, xs[1] + pw / 2, 20, 'échange de 2 racines', 'varie', 's')
arrow(ax, (x1 - 1.0, y1 + 3.2), (x2 + 3.4, y2 + 1.0), 'autre', lw=0.9, curve=0.35)
arrow(ax, (x3 + 3.4, y3 - 1.0), (x1 - 1.0, y1 - 3.2), 'autre', lw=0.9, curve=0.35)
text(ax, xs[1] + pw / 2, 13, 'et des circuits', 'autre', 's')
# step 3
cx = xs[2] + pw / 2
text(ax, cx, 42, r'$S_3$', 'resultat', 'xl', weight='bold')
text(ax, cx, 32, '6 permutations', 'resultat', 's')
text(ax, cx, 24, 'toutes celles de 3\nobjets', 'resultat', 's')
arrow(ax, (xs[0] + pw + 0.3, 36), (xs[1] - 0.3, 36), 'fixe', lw=0.8)
arrow(ax, (xs[1] + pw + 0.3, 36), (xs[2] - 0.3, 36), 'fixe', lw=0.8)
save(fig, '65-033')
