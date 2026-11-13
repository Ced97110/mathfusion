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
text(ax, 44, 79, r"$x'$ : image de $x$ ; $y'$ : image de $y$", 'encre', 's')
box(ax, 2, 54, 32, 10, 'sujet', label=r'$R$ : produit $yx$', size='s'); box(ax, 54, 54, 32, 10, 'autre', label=r"$(yx)'=x'y'$", size='s')
arrow(ax, (35, 59), (53, 59), 'varie'); text(ax, 44, 66, r"$R\to R'$", 'varie', 's')
text(ax, 44, 49, "ordre renversé : $yx$ → $x'y'$", 'varie', 's')
line(ax, [(2, 42), (86, 42)], 'fixe', lw=0.5, dash=True)
box(ax, 2, 24, 32, 10, 'sujet', label=r'$R^0$ : $x\times y=yx$', size='s'); box(ax, 54, 24, 32, 10, 'autre', label=r"$(yx)'=x'y'$", size='s')
arrow(ax, (35, 29), (53, 29), 'varie'); text(ax, 44, 36, r"$R^0\to R'$", 'varie', 's')
text(ax, 44, 19, "ordre gardé : $x\\times y$ → $x'y'$", 'resultat', 's')
text(ax, 44, 7, 'même application, deux lectures', 'encre', 's')
save(fig, '52-224')
