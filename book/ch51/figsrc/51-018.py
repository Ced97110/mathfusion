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
text(ax, 22, 57, 'heure', 'sujet', 's'); text(ax, 50, 57, 'opposé', 'varie', 's')
for i, (a, b) in enumerate([(0, 0), (1, 3), (2, 2), (3, 1)]):
    y = 40 - i * 12
    box(ax, 17, y, 10, 9, 'sujet', label=str(a), r=0.5)
    box(ax, 45, y, 10, 9, 'varie', label=str(b), r=0.5)
    box(ax, 65, y, 10, 9, 'resultat', label='0', r=0.5)
    plus(ax, 36, y + 4.5); equals(ax, 60, y + 4.5)
save(fig, '51-018')
