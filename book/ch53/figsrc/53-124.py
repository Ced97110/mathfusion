import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
heads = [('départ', 'sujet'), ('étape décisive', 'varie'), ('arrivée', 'resultat')]
labels = ['m = 2\npremier avec 55', 'ordre k = 20\ndivise 40', r'$2^{40}\equiv 1$']
xs = [2, 32, 62]
for (h, r), lab, x in zip(heads, labels, xs):
    text(ax, x + 12, 76, h, r, 's')
    box(ax, x, 58, 24, 14, r, label=lab, size='s', lw=1.4 if r == 'varie' else 0.8)
arrow(ax, (26.5, 65), (31.5, 65), 'fixe')
arrow(ax, (56.5, 65), (61.5, 65), 'fixe')
# 40 = 20 × 2 : deux blocs de 20 facteurs, chacun de reste 1
box(ax, 8, 22, 36, 11, 'sujet', label=r'$2^{20}\equiv 1$')
box(ax, 44, 22, 36, 11, 'sujet', label=r'$2^{20}\equiv 1$')
brace(ax, 8, 80, 22, 'sujet', label=r'exposant $40=20\times2$')
arrow(ax, (44, 57.5), (44, 33.5), 'varie')
save(fig, '53-124')
