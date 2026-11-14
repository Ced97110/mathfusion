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

fig, ax = canvas(100)
text(ax, 44, 96, r'$(2\cdot3)\cdot4=2\cdot(3\cdot4)=24$ : associatif', 'resultat', 's')
box(ax, 14, 62, 60, 28, 'sujet', fill=False)
text(ax, 44, 85, r'dans $R$ : produit $a-b$', 'sujet', 's')
text(ax, 44, 79, r'$(5-3)-1=1$', 'sujet', 's'); text(ax, 44, 73, r'$5-(3-1)=3$', 'sujet', 's')
text(ax, 44, 66.5, r'$\neq$', 'limite', 'l')
arrow(ax, (44, 61), (44, 47), 'varie')
text(ax, 48, 54, 'on renverse le produit', 'varie', 's', ha='left')
box(ax, 14, 14, 60, 32, 'autre', fill=False)
text(ax, 44, 41, r'dans $R^0$ : $a*b=b-a$', 'autre', 's')
text(ax, 44, 35, r'$(5*3)*1=3$', 'autre', 's'); text(ax, 44, 29, r'$5*(3*1)=-7$', 'autre', 's')
text(ax, 44, 22.5, r'$\neq$', 'limite', 'l')
text(ax, 44, 7, r'$R$ non associatif : $R^0$ aussi', 'encre', 's')
save(fig, '52-223')
