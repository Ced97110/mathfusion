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

fig, ax = canvas(60)
text(ax, 20, 55, 'dans $F(u)$', 'sujet', 's')
mat2(ax, 20, 40, ['0','1'], ['1','2'], 'sujet')
text(ax, 20, 28, 'compagnon', 'sujet', 's')
text(ax, 20, 15, r'$T=2,\ \det=-1$', 'sujet', 's')
arrow(ax, (40, 36), (50, 36), 'varie'); text(ax, 45, 41, 'scalaire', 'varie', 's')
text(ax, 69, 55, 'dans $L$', 'resultat', 's')
box(ax, 53, 34, 15, 11, 'sujet', label='$C$'); box(ax, 69, 34, 15, 11, 'fixe', label='0')
box(ax, 53, 22, 15, 11, 'fixe', label='0'); box(ax, 69, 22, 15, 11, 'sujet', label='$C$')
text(ax, 69, 17, '$C$ deux fois', 'varie', 's')
text(ax, 69, 9, r'$T=4,\ \det=1$', 'resultat', 's')
save(fig, '77-125')
