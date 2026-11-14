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

fig, ax = canvas(44)
text(ax, 10, 38, r'$P^2$', 'sujet', 'm')
mat2(ax, 10, 23, ['3','4'], ['2','3'], 'sujet')
arrow(ax, (19, 23), (31, 23), 'varie'); text(ax, 25, 28, r'$-3\cdot 1$', 'varie', 's')
text(ax, 41, 38, r'matrice de $2\sqrt{2}$', 'sujet', 's')
mat2(ax, 41, 23, ['0','4'], ['2','0'], 'sujet')
arrow(ax, (50, 23), (62, 23), 'varie'); text(ax, 56, 28, r'$\det$', 'varie', 's')
text(ax, 75, 27, r'$0\times0-4\times2$', 'resultat', 's')
text(ax, 75, 18, r'$=-8$', 'resultat', 'l', weight='bold')
save(fig, '77-120')
