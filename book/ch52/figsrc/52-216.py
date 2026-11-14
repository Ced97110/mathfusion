import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, rows, role='sujet', c=6.5, fills=None, size='m'):
    n = len(rows); m = len(rows[0]); x0 = cx - m * c / 2; y0 = cy - n * c / 2
    for (i, j), r in (fills or {}).items():
        box(ax, x0 + j * c + 0.4, y0 + (n - 1 - i) * c + 0.4, c - 0.8, c - 0.8, r, r=0.3, lw=0.4)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            if v != '': text(ax, x0 + (j + .5) * c, y0 + (n - 1 - i + .5) * c, str(v), role, size)
    for sx, d in ((x0 - 0.8, 1), (x0 + m * c + 0.8, -1)):
        line(ax, [(sx + d * 1.4, y0 - 0.5), (sx, y0 - 0.5), (sx, y0 + n * c + 0.5), (sx + d * 1.4, y0 + n * c + 0.5)], role, lw=1.0)

def cross(ax, x, y, role='encre'):
    line(ax, [(x - 1.5, y - 1.5), (x + 1.5, y + 1.5)], role); line(ax, [(x - 1.5, y + 1.5), (x + 1.5, y - 1.5)], role)

def eq(ax, x, y, role='encre'):
    line(ax, [(x - 1.6, y + 0.9), (x + 1.6, y + 0.9)], role); line(ax, [(x - 1.6, y - 0.9), (x + 1.6, y - 0.9)], role)

fig, ax = canvas(84)
def pair(cx, y, a, b, ra, rb):
    box(ax, cx - 8.5, y, 7, 7, ra, label=a, size='s'); box(ax, cx + 1.5, y, 7, 7, rb, label=b, size='s')
for cx, name, role in ((22, 'anti-isomorphisme', 'sujet'), (66, 'isomorphisme', 'autre')):
    text(ax, cx, 76, name, role, 'm')
    pair(cx, 58, r'$x$', r'$y$', 'sujet', 'varie')
    arrow(ax, (cx, 56), (cx, 45), 'fixe')
pair(22, 37, r"$y'$", r"$x'$", 'varie', 'sujet')
pair(66, 37, r"$x'$", r"$y'$", 'sujet', 'varie')
text(ax, 22, 30, 'ordre renversé', 'sujet', 's'); text(ax, 66, 30, 'ordre gardé', 'autre', 's')
box(ax, 4, 6, 80, 12, 'fixe', label=r'somme respectée · $1\mapsto1$', size='s')
save(fig, '52-216')
