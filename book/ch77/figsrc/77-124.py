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

fig, ax = canvas(62)
box(ax, 4, 48, 26, 10, 'fixe', label='$L$')
box(ax, 4, 28, 26, 10, 'sujet', label='$F(u)$')
box(ax, 4, 8, 26, 10, 'fixe', label='$F$')
line(ax, [(17, 48), (17, 38)], 'fixe'); line(ax, [(17, 28), (17, 18)], 'fixe')
text(ax, 20, 43, r'degré $r=2$', 'varie', 's', ha='left'); text(ax, 20, 23, r'degré $m=2$', 'sujet', 's', ha='left')
box(ax, 44, 44, 42, 12, 'sujet', label=r'$\lambda^2-2\lambda-1$')
text(ax, 65, 38, r'$a_1=2,\ a_2=-1$', 'sujet', 's')
box(ax, 44, 20, 42, 10, 'resultat', label=r'trace $T=2\times2=4$', size='s')
box(ax, 44, 6, 42, 10, 'resultat', label=r'norme $N=(-1)^2=1$', size='s')
save(fig, '77-124')
