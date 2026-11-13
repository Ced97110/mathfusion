import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 74, 'Éléments inversibles de ℤ/8', 'sujet', 'm')
xs = [12, 33, 55, 76]
sq = [r'$1^2=1$', r'$3^2=9\equiv 1$', r'$5^2=25\equiv 1$', r'$7^2=49\equiv 1$']
for x, a, s in zip(xs, [1, 3, 5, 7], sq):
    disc(ax, x, 60, 4.5, 'sujet', label=str(a))
    arrow(ax, (x, 55), (x, 46), 'varie')
    text(ax, x, 40, s, 'varie', 's')
    arrow(ax, (x, 36), (x, 31), 'resultat')
box(ax, 6, 22, 76, 8, 'resultat', label='tous les carrés valent 1', size='s')
arrow(ax, (44, 21), (44, 14), 'limite')
box(ax, 6, 3, 76, 10, 'limite', label='aucun n’engendre les quatre', size='m')
save(fig, '54-263')
