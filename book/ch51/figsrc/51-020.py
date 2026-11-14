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
text(ax, 18, 44, r'$2\times b=2$', 'sujet', 'l')
arrow(ax, (31, 44), (39.5, 44), 'fixe')
box(ax, 40, 39, 20, 10, 'resultat', label=r'$b=1$', r=0.5)
box(ax, 63, 39, 20, 10, 'resultat', label=r'$b=3$', r=0.5)
text(ax, 50, 33, r'$2\times1=2$', 'resultat', 's')
text(ax, 73, 33, r'$2\times3=6$, soit $2$', 'resultat', 's')
text(ax, 61.5, 26, 'deux solutions', 'resultat', 's')
text(ax, 18, 10, r'$2\times b=1$', 'sujet', 'l')
arrow(ax, (31, 10), (39.5, 10), 'fixe')
box(ax, 40, 5, 43, 10, 'limite', fill=False, dash=True, label=r'aucun $b$ ne convient', r=0.5)
save(fig, '51-020')
