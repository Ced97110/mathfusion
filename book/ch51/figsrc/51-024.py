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
box(ax, 3, 10, 82, 50, 'resultat', fill=False, lw=1.2)
text(ax, 44, 55, 'anneau', 'resultat', 'l')
box(ax, 7, 31, 36, 18, 'sujet'); box(ax, 45, 31, 36, 18, 'autre')
text(ax, 25, 43.5, r'$(R,+,0)$', 'sujet', 'm'); text(ax, 25, 36, 'groupe commutatif', 'sujet', 's')
text(ax, 63, 43.5, r'$(R,\cdot,1)$', 'autre', 'm'); text(ax, 63, 36, 'monoïde', 'autre', 's')
box(ax, 20, 13, 48, 12, 'varie')
text(ax, 44, 21.5, 'distributivité', 'varie', 's'); text(ax, 44, 16.5, r'$a(b+c)=ab+ac$', 'varie', 's')
arrow(ax, (34, 25.5), (25, 30.5), 'varie'); arrow(ax, (54, 25.5), (63, 30.5), 'varie')
save(fig, '51-024')
