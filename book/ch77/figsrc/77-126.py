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

fig, ax = canvas(56)
brace(ax, 30, 62, 46, 'fixe', label=r'$\sqrt{2}$ répété 2 fois', down=False)
text(ax, 15, 39, r'$a_1=0$', 'sujet', 'm'); text(ax, 15, 23, r'$a_2=-2$', 'sujet', 'm')
for c, x in enumerate((30, 48)):
    box(ax, x, 34, 14, 10, 'sujet', label='0'); box(ax, x, 18, 14, 10, 'sujet', label='$-2$')
arrow(ax, (64, 39), (68, 39), 'resultat'); arrow(ax, (64, 23), (68, 23), 'resultat')
text(ax, 78, 39, r'$T=0+0=0$', 'resultat', 's')
text(ax, 78, 23, r'$N=(-2)^2=4$', 'resultat', 's')
text(ax, 78, 14, r'et non $-2$', 'limite', 's')
save(fig, '77-126')
