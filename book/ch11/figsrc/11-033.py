import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 50, 34, 9, 'fixe', label='250 grammes')
arrow(ax, (38, 54.5), (50, 54.5), 'varie')
box(ax, 52, 50, 34, 9, 'sujet', label=r'250 $g$')
for y, p, res, desc in [(28, 'k', 'kg', 'mille grammes'), (8, 'm', 'mg', 'un millième de gramme')]:
    box(ax, 2, y, 12, 10, 'varie', label=r'$%s$' % p)
    box(ax, 16, y, 12, 10, 'sujet', label=r'$g$')
    text(ax, 33, y + 5, '=', 'encre', 'l')
    box(ax, 38, y, 16, 10, 'resultat', label=r'$%s$' % res)
    text(ax, 58, y + 5, desc, 'encre', 's', ha='left')
save(fig, '11-033')
