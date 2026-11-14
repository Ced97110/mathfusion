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

fig, ax = canvas(70)
text(ax, 44, 64, 'le 0 (gris) ne change rien', 'encre', 's')
def row(y, lab, v):
    text(ax, 2, y + 5, lab, 'encre', 's', ha='left')
    box(ax, 22, y, 12, 10, 'sujet', label=str(v), r=0.5); plus(ax, 38, y + 5)
    box(ax, 42, y, 12, 10, 'fixe', label='0', r=0.5); equals(ax, 58, y + 5)
    box(ax, 62, y, 12, 10, 'resultat', label=str(v), r=0.5)
row(47, 'entiers', 5); row(31, 'cadran', 3)
text(ax, 2, 14, 'tableaux', 'encre', 's', ha='left')
grid(ax, 22, 8, 6, 2, 'sujet'); plus(ax, 38, 14)
grid(ax, 42, 8, 6, 2, 'fixe')
for r_ in range(2):
    for c in range(2): text(ax, 45 + c * 6, 17 - r_ * 6, '0', 'fixe', 's')
equals(ax, 58, 14); grid(ax, 62, 8, 6, 2, 'resultat')
save(fig, '51-028')
