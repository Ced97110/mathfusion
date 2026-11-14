import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 2, 8, 84, 36, 'autre', fill=False, dash=True)
text(ax, 44, 39, r'calcul dans $H$ (cadran)', 'autre', 's')
bw = 14
for x, h, v in ((8, r'$h_1$', '1'), (34, r'$h_2$', '2')):
    text(ax, x + bw / 2, 30, h, 'autre', 'm'); box(ax, x, 15, bw, 11, 'autre', label=v, size='l')
text(ax, 29, 20.5, '+', 'varie', 'l'); text(ax, 55, 20.5, '=', 'varie', 'l')
text(ax, 69, 30, r'$h_1h_2$', 'resultat', 'm'); box(ax, 62, 15, bw, 11, 'resultat', label='0', size='l')
text(ax, 44, 11, '1+2=3, reste 0', 'fixe', 's')
save(fig, '45-158')
