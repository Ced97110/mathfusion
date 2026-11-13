import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def plus(ax, x, y, r="fixe", s=1.3):
    line(ax, [(x - s, y), (x + s, y)], r, 1.0); line(ax, [(x, y - s), (x, y + s)], r, 1.0)

def equals(ax, x, y, r="fixe", s=1.3):
    line(ax, [(x - s, y + .6), (x + s, y + .6)], r, 1.0); line(ax, [(x - s, y - .6), (x + s, y - .6)], r, 1.0)

def cross(ax, x, y, r="fixe", s=1.0):
    line(ax, [(x - s, y - s), (x + s, y + s)], r, 1.0); line(ax, [(x - s, y + s), (x + s, y - s)], r, 1.0)

def grid(ax, x0, y0, cs, n, role="fixe"):
    for r in range(n):
        for c in range(n):
            box(ax, x0 + c * cs, y0 + (n - 1 - r) * cs, cs, cs, role, r=0.4, lw=0.6)

fig, ax = canvas(66)
cx = [26, 42, 58, 74]
text(ax, 2, 54, r'$b$', 'sujet', 'm', ha='left'); text(ax, 2, 20, r'$2\times b$', 'resultat', 'm', ha='left')
res = {0: 0, 1: 2, 2: 0, 3: 2}
for b in range(4):
    box(ax, cx[b] - 5.5, 49.5, 11, 9, 'sujet', label=str(b), r=0.5)
    if b in (0, 2): box(ax, cx[b] - 5.5, 15.5, 11, 9, 'resultat', label=str(b), r=0.5)
    else: box(ax, cx[b] - 5.5, 15.5, 11, 9, 'limite', fill=False, dash=True, label=str(b), r=0.5)
for b, v in res.items():
    arrow(ax, (cx[b], 49), (cx[v], 25), 'varie')
text(ax, 44, 10, r'$1$ et $3$ : jamais atteints', 'limite', 's')
text(ax, 44, 4, r'$2$ vient de $b=1$ et $b=3$', 'resultat', 's')
save(fig, '51-019')
