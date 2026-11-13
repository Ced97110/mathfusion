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

fig, ax = canvas(64)
box(ax, 3, 26, 82, 34, 'sujet', fill=False, lw=1.2)
text(ax, 44, 55, 'nombres pairs', 'sujet', 'm')
box(ax, 16, 33, 12, 10, 'sujet', label='2', r=0.5); cross(ax, 33, 38)
box(ax, 38, 33, 12, 10, 'sujet', label='4', r=0.5); equals(ax, 55, 38, 'resultat')
box(ax, 60, 33, 12, 10, 'resultat', label='8', r=0.5)
arrow(ax, (22, 25.5), (22, 16.5), 'limite')
box(ax, 16, 5, 12, 10, 'limite', fill=False, dash=True, label='1', r=0.5)
text(ax, 34, 10, "n'est pas pair : pas de 1", 'limite', 's', ha='left')
save(fig, '51-031')
