import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# pour le sac e_2, on lit la colonne 2 du tableau
cw, ch = 10, 9
x1, x2 = 24, 36
box(ax, x2 - 3, 52, cw + 6, 9, 'varie', label=r'sac $e_2$', size='m', r=0.6)
arrow(ax, (x2 + cw / 2, 52), (x2 + cw / 2, 44.5), 'varie', lw=1.4)
for (x, role, vals) in [(x1, 'fixe', ('2', '1')), (x2, 'varie', ('1', '3'))]:
    box(ax, x, 34, cw, ch, role, label=vals[0], size='m', r=0.5)
    box(ax, x, 24, cw, ch, role, label=vals[1], size='m', r=0.5)
text(ax, x1 + cw / 2, 20.5, 'colonne 1', 'fixe', 's')
text(ax, x2 + cw / 2 + 2, 20, 'colonne 2', 'varie', 's', weight='bold', ha='left')
box(ax, 22, 5, 30, 8, 'resultat', label=r'$\eta(e_2) = (1, 3)$', size='s', r=0.5)
arrow(ax, (x2 + cw / 2, 23.5), (x2 + cw / 2, 14), 'resultat', lw=1.4)
text(ax, 70, 38, 'on lit\nla colonne 2', 'varie', 's')
save(fig, '58-201')
