import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
line(ax, [(5, 50), (83, 50)], 'sujet', lw=1.4)
px = [16, 44, 72]
for x, l in zip(px, (2, 4, 1)):
    disc(ax, x, 50, 2.2, 'resultat'); text(ax, x, 56, '$e_{%d}$' % l, 'encre', 'm')
arrow(ax, (19.5, 50), (40.5, 50), 'varie'); arrow(ax, (47.5, 50), (68.5, 50), 'varie')
arrow(ax, (72, 46), (16, 46), 'varie', curve=-0.3)
box(ax, 2, 20, 26, 9, 'resultat', label='$e_1e_2=e_4$')
box(ax, 31, 20, 26, 9, 'fixe', label='$e_2e_4=e_1$')
box(ax, 60, 20, 26, 9, 'fixe', label='$e_4e_1=e_2$')
text(ax, 14, 6.5, 'sens inverse', 'varie', 's')
box(ax, 28, 2, 32, 9, 'autre', label='$e_2e_1=-e_4$')
save(fig, '78-141')
