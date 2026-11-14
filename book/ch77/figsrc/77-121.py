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

fig, ax = canvas(68)
box(ax, 3, 28, 12, 12, 'sujet', label='$u$', size='l')
text(ax, 35, 63, 'les 4 images de $u$', 'encre', 's')
ys = [52, 40, 28, 16]
for i, y in enumerate(ys):
    box(ax, 24, y, 22, 9, 'fixe', label=r'$\sigma_%d(u)$' % (i + 1))
    arrow(ax, (15, 34), (24, y + 4.5), 'varie')
    line(ax, [(46, y + 4.5), (50, y + 4.5)], 'fixe')
line(ax, [(50, 20.5), (50, 56.5)], 'fixe')
box(ax, 56, 40, 30, 14, 'resultat', label=r'somme : $T=4$', size='s')
box(ax, 56, 18, 30, 14, 'resultat', label=r'produit : $N=-8$', size='s')
arrow(ax, (50, 47), (56, 47), 'resultat'); arrow(ax, (50, 25), (56, 25), 'resultat')
save(fig, '77-121')
