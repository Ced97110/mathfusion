import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
for x, s in ((4, '(1 ; 2)'), (34, '(3 ; 1)'), (64, '(4 ; 3)')): box(ax, x, 58, 20, 9, 'sujet', label=s)
text(ax, 29, 62.5, '+', 'encre', 'l'); text(ax, 59, 62.5, '=', 'encre', 'l')
for x, s in ((4, '4 €'), (34, '7 €'), (64, '11 €')):
    arrow(ax, (x + 10, 57), (x + 10, 46), 'fixe'); box(ax, x, 36, 20, 9, 'resultat', label=s)
box(ax, 4, 18, 20, 9, 'sujet', label='(1 ; 2)'); box(ax, 34, 18, 20, 9, 'sujet', label='(3 ; 6)')
arrow(ax, (26, 22.5), (32, 22.5), 'varie'); text(ax, 29, 27.5, r'$\times 3$', 'varie')
arrow(ax, (14, 17), (14, 12), 'fixe'); arrow(ax, (44, 17), (44, 12), 'fixe')
box(ax, 4, 3, 20, 9, 'resultat', label='4 €'); box(ax, 34, 3, 20, 9, 'resultat', label='12 €')
save(fig, '71-035')
