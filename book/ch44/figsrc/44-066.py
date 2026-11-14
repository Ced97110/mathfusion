import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'Règle : $x\star y = y$ (le résultat est le second)', 'encre', 's')
for i, (role, n) in enumerate([('sujet', 'R'), ('autre', 'B')]):
    y = 38 - i * 17
    disc(ax, 12, y + 5, 5, role, label=n, size='l')
    text(ax, 33, y + 5, rf'${n}\star x = x$', role, 'm')
    arrow(ax, (47, y + 5), (53, y + 5), 'fixe')
    box(ax, 54, y, 30, 10, 'resultat', label='neutre à gauche', size='s')
box(ax, 8, 4, 72, 11, 'limite', label='deux neutres à gauche : pas unique', size='s')
save(fig, '44-066')
