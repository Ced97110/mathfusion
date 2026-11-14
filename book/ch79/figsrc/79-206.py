import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
S = 8.0; PITCH = 9.0; X0 = 36.0
fig, ax = canvas(88)
data = [('2', 2, 2), ('3', 1, 0), ('5', 0, 1)]
for k, (p, e12, e20) in enumerate(data):
    top = 84 - 24 * k
    m = min(e12, e20)
    text(ax, 3, top - 8.5, 'facteur ' + p, 'encre', 's', ha='left')
    for r_, (lab, e, role) in enumerate([('12', e12, 'sujet'), ('20', e20, 'autre')]):
        y = top - 8 - 9 * r_
        text(ax, 28, y + 4, lab, role, 's')
        if e == 0:
            box(ax, X0, y, S, S, 'fixe', fill=False, dash=True, label='0', size='s')
        for i in range(e):
            box(ax, X0 + PITCH * i, y, S, S, 'resultat' if i < m else role)
text(ax, 44, 13, r'PGCD (le vert) : $4$', 'resultat', 'm')
text(ax, 44, 5, r'PPCM (le plus long) : $60$', 'varie', 'm')
save(fig, '79-206')
