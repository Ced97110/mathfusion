import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
R = 4
text(ax, 44, 74, r'degré 2 : $\eta$ échange les deux racines', 'encre', 's')
# avant et après l'échange
disc(ax, 24, 58, R, 'sujet', label=r'$r_1$')
disc(ax, 64, 58, R, 'autre', label=r'$r_2$')
arrow(ax, (29, 61.5), (59, 61.5), 'varie', curve=-0.2)
arrow(ax, (59, 54.5), (29, 54.5), 'varie', curve=-0.2)
text(ax, 44, 48, r'$\eta$', 'varie', 'l')
# la combinaison avant et après
box(ax, 2, 24, 38, 12, 'sujet', label=r'$r_1-r_2$')
box(ax, 48, 24, 38, 12, 'varie', label=r'$r_2-r_1$')
arrow(ax, (40.5, 30), (47.5, 30), 'varie')
text(ax, 44, 40, r'$\eta$', 'varie', 's')
text(ax, 21, 19, 'avant', 'sujet', 's')
text(ax, 67, 19, 'après : signe changé', 'varie', 's')
box(ax, 10, 3, 68, 11, 'resultat', label=r'$(r_1-r_2)^2=(r_2-r_1)^2$', size='s')
save(fig, '64-159')
