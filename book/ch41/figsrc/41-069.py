import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u, v = (1, 3), (4, 2)
assert 2 * u[0] == 2 and 2 * u[1] == 6 and u[0] + v[0] == 5 and u[1] + v[1] == 5 and u[0] * v[0] + u[1] * v[1] == 10
rows = [(50, r'$2\times u$', 'un nombre, un vecteur', (2, 6), 'fixe'),
        (30, r'$u+v$', 'deux vecteurs', (5, 5), 'fixe'),
        (10, r'$u\cdot v$', 'deux vecteurs', None, 'sujet')]
for y, lab, ins, res, role in rows:
    box(ax, 2, y - 6, 20, 12, role, label=lab, size='m')
    text(ax, 40, y + 8.5, ins, 'fixe', 's')
    arrow(ax, (24, y), (56, y), role, lw=1.2)
    if res is not None:
        o = (60, y - 4.5)
        arrow(ax, o, (o[0] + 1.6 * res[0], o[1] + 1.6 * res[1]), 'autre', lw=1.8)
        text(ax, 76, y, r'$\langle %d;\ %d\rangle$' % res, 'autre', 's')
    else:
        box(ax, 62, y - 6, 24, 12, 'resultat', label='10', size='l', weight='bold')
save(fig, '41-069')
