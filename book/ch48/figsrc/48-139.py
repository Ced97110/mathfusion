import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 8, 44, 50, 'sujet', fill=False); text(ax, 24, 54, 'S₃ : 6 permutations', 'sujet', 's')
box(ax, 5, 33, 38, 15, 'resultat'); text(ax, 24, 44.5, 'noyau A₃', 'resultat', 's')
for i, t in enumerate(['id', 'circ. 1', 'circ. 2']):
    box(ax, 7 + i * 12, 35, 11, 6, 'resultat', fill=False, label=t, size='s', r=0.5)
box(ax, 5, 11, 38, 15, 'varie')
for i, t in enumerate(['éch. 12', 'éch. 13', 'éch. 23']):
    box(ax, 7 + i * 12, 13, 11, 6, 'varie', fill=False, label=t, size='s', r=0.5)
box(ax, 62, 8, 24, 50, 'autre', fill=False); text(ax, 74, 54, '{1, −1}', 'autre', 's')
disc(ax, 74, 40.5, 4, 'resultat', label='1', size='m'); disc(ax, 74, 18.5, 4, 'varie', label='−1', size='m')
arrow(ax, (43, 40.5), (69.8, 40.5), 'resultat'); arrow(ax, (43, 18.5), (69.8, 18.5), 'varie')
text(ax, 54, 46, 'sg', 'encre', 'm')
save(fig, '48-139')
