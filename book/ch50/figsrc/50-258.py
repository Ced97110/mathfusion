import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
line(ax, [(44, 4), (44, 62)], 'fixe', dash=True)
for cx, o, n, res, rr in [(22, 'ordre 6', r'$n_2 = 3$', 'groupe du triangle', 'resultat'), (66, 'ordre 21', r'$n_3 = 7$', 'existe ?', 'varie')]:
    text(ax, cx, 60, o, 'encre', 'l', weight='bold')
    box(ax, cx - 13, 44, 26, 9, 'sujet', label=n)
    arrow(ax, (cx, 43), (cx, 37), 'fixe')
    box(ax, cx - 11, 28, 22, 8, 'resultat', label='test passé', size='s')
    arrow(ax, (cx, 27), (cx, 21), 'fixe')
    box(ax, cx - 18, 10, 36, 10, rr, label=res, size='s', dash=(rr == 'varie'), fill=(rr != 'varie'))
save(fig, '50-258')
