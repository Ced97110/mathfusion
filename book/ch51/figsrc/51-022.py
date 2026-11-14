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

fig, ax = canvas(80)
text(ax, 20, 76, "d'abord la somme", 'sujet', 's')
box(ax, 4, 64, 32, 9, 'sujet', label=r'$1+2=3$', r=0.5)
box(ax, 40, 64, 28, 9, 'sujet', label=r'$3\times3=9$, soit $1$', r=0.5)
arrow(ax, (36.5, 68.5), (39.5, 68.5), 'sujet')
text(ax, 24, 54, "d'abord les produits", 'autre', 's')
box(ax, 4, 40, 32, 9, 'autre', label=r'$3\times1=3$', r=0.5)
box(ax, 4, 28, 32, 9, 'autre', label=r'$3\times2=6$, soit $2$', r=0.5)
box(ax, 40, 34, 28, 9, 'autre', label=r'$3+2=5$, soit $1$', r=0.5)
arrow(ax, (36.5, 44.5), (40, 41), 'autre'); arrow(ax, (36.5, 32.5), (40, 36), 'autre')
box(ax, 72, 49, 12, 9, 'resultat', label='1', r=0.5)
arrow(ax, (68.5, 68.5), (78, 58.5), 'resultat'); arrow(ax, (68.5, 38.5), (78, 48.5), 'resultat')
text(ax, 78, 44.5, 'même résultat', 'resultat', 's')
save(fig, '51-022')
