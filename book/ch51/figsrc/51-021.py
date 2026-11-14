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
grid(ax, 4, 36, 6.5, 4, 'sujet'); grid(ax, 58, 36, 6.5, 4, 'autre')
text(ax, 17, 66, 'addition', 'sujet', 's'); text(ax, 71, 66, 'multiplication', 'autre', 's')
arrow(ax, (32, 49), (56, 49), 'varie', both=True)
text(ax, 44, 55, 'distributivité', 'varie', 's')
text(ax, 22, 16, r'$3\times(1+2)$', 'sujet', 'm'); text(ax, 66, 16, r'$3\times1+3\times2$', 'autre', 'm')
equals(ax, 44, 16, 'resultat')
text(ax, 22, 8, "somme d'abord", 'sujet', 's'); text(ax, 66, 8, "produits d'abord", 'autre', 's')
save(fig, '51-021')
