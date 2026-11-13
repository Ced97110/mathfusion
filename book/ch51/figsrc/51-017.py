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

fig, ax = canvas(62)
x0, y0, cs = 4, 6, 10.5
for r in range(4):
    for c in range(4):
        role = 'resultat' if r == 2 else ('varie' if (r, c) in [(0, 1), (1, 0)] else 'fixe')
        box(ax, x0 + c * cs, y0 + (3 - r) * cs, cs, cs, role, r=0.4, lw=0.6)
ctr = lambda r, c: (x0 + (c + .5) * cs, y0 + (3 - r + .5) * cs)
line(ax, [(x0, y0 + 4 * cs), (x0 + 4 * cs, y0)], 'fixe', dash=True)
text(ax, *ctr(0, 1), '1', 'varie'); text(ax, *ctr(1, 0), '1', 'varie')
a, b = ctr(0, 1), ctr(1, 0)
arrow(ax, (a[0] - 3, a[1] - 3), (b[0] + 3, b[1] + 3), 'varie', both=True)
text(ax, 25, 54, "table d'addition", 'sujet', 'm')
text(ax, 67, 48, r'$a+b=b+a$', 'varie', 'm')
text(ax, 67, 41, 'symétrique', 'varie', 's')
rc = ctr(2, 3)
arrow(ax, (x0 + 4 * cs + .5, rc[1]), (50.5, rc[1]), 'resultat')
for i, v in enumerate([2, 3, 0, 1]):
    box(ax, 51 + 8 * i, rc[1] - 4, 7.5, 8, 'resultat', label=str(v), r=0.5)
text(ax, 67, rc[1] + 8, 'ligne 2', 'resultat', 's')
text(ax, 67, rc[1] - 8, 'chaque heure 1 fois', 'resultat', 's')
save(fig, '51-017')
