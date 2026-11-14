import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

EM = ' '
def pitch(size='m'):
    return 1.636 * SIZE[size] * 25.4 / 72
def rowstr(vals):
    return EM.join(vals)
def brk(ax, cx, cy, hw, hh, role='encre'):
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.3, cy + hh), (x, cy + hh), (x, cy - hh), (x - s * 1.3, cy - hh)], role, lw=0.8)
def mat2(ax, cx, cy, r1, r2, role='encre', size='m'):
    text(ax, cx, cy + 3.2, rowstr(r1), role, size); text(ax, cx, cy - 3.2, rowstr(r2), role, size)
    brk(ax, cx, cy, 4.8, 5.4, role)

fig, ax = canvas(64)
text(ax, 19.5, 58, r'$A$ : coefficients dans $\mathbb{R}$', 'sujet', 's')
box(ax, 3, 40, 34, 12, 'sujet', label=r'$a+b\,i$')
text(ax, 20, 35, r'$a$ et $b$ réels', 'sujet', 's')
arrow(ax, (39, 46), (51, 46), 'varie'); text(ax, 45, 51, r'$\mathbb{R}\to\mathbb{C}$', 'varie', 's')
text(ax, 69, 58, r'$A_K$ : coefficients dans $\mathbb{C}$', 'autre', 's')
box(ax, 52, 40, 34, 12, 'autre', label=r'$z+w\,j$')
text(ax, 69, 35, r'$z$ et $w$ complexes', 'autre', 's')
box(ax, 3, 6, 83, 22, 'fixe')
text(ax, 44.5, 21, 'même base, même table', 'fixe', 'm')
text(ax, 44.5, 12, r'$i\cdot i=-1$ et $j\cdot j=-1$', 'fixe', 'm')
save(fig, '77-128')
