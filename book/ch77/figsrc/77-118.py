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

fig, ax = canvas(52)
box(ax, 22, 26, 18, 14, 'resultat', label=r'$P$', size='l')
box(ax, 40, 26, 18, 14, 'fixe', label=r'$3\cdot 1$', size='l')
box(ax, 22, 12, 18, 14, 'fixe', label='1', size='l')
box(ax, 40, 12, 18, 14, 'resultat', label=r'$P$', size='l')
text(ax, 11, 33, 'trace 2', 'resultat', 's')
text(ax, 70, 19, 'trace 2', 'resultat', 's')
text(ax, 40, 46, 'blocs diagonaux en vert', 'resultat', 's')
text(ax, 40, 5, r'$2+2=4$', 'resultat', 'l')
save(fig, '77-118')
