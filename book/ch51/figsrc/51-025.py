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
box(ax, 4, 20, 22, 22, 'sujet', label=r'$R$', size='xl')
text(ax, 15, 13, r'soit $R$ un anneau', 'sujet', 's')
text(ax, 66, 57, r'$R$ tient la place de :', 'varie', 's')
for y, s in [(44, 'les entiers'), (29, 'les 4 heures du cadran'), (14, 'tableaux de nombres')]:
    box(ax, 46, y, 40, 10, 'fixe', label=s, size='s', r=0.5)
    arrow(ax, (26.5, 31), (45.5, y + 5), 'varie')
save(fig, '51-025')
