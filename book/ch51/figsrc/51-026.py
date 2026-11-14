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

fig, ax = canvas(76)
box(ax, 3, 31, 16, 18, 'sujet', label='+', size='xl')
for y, s in [(62, 'entiers : 3 + 4 = 7'), (44, 'cadran à 4 h : 3 + 2 = 1')]:
    box(ax, 28, y, 56, 11, 'varie', label=s, size='s', r=0.5)
    arrow(ax, (19.5, 40), (27.5, y + 5.5), 'fixe')
box(ax, 28, 6, 56, 32, 'varie', r=0.5)
text(ax, 56, 32, 'tableaux : case par case', 'varie', 's')
arrow(ax, (19.5, 40), (27.5, 22), 'fixe')
grid(ax, 33, 11, 5, 2); plus(ax, 48, 16); grid(ax, 53, 11, 5, 2); equals(ax, 68, 16); grid(ax, 73, 11, 5, 2)
save(fig, '51-026')
