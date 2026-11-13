import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 15, 56, 'diviseurs de 3', 'sujet', 'm'); text(ax, 73, 56, 'diviseurs de 5', 'autre', 'm')
box(ax, 8, 40, 14, 9, 'sujet', label='1'); box(ax, 8, 22, 14, 9, 'sujet', label='3')
box(ax, 66, 40, 14, 9, 'autre', label='1'); box(ax, 66, 22, 14, 9, 'autre', label='5')
for x0, x1 in [(9, 21), (67, 79)]:
    line(ax, [(x0, 23), (x1, 30)], 'limite', lw=1.1)
box(ax, 32, 40, 24, 9, 'resultat', label='1 en commun', size='s')
arrow(ax, (22.5, 44.5), (31.5, 44.5), 'fixe'); arrow(ax, (65.5, 44.5), (56.5, 44.5), 'fixe')
arrow(ax, (44, 39), (44, 16), 'resultat')
box(ax, 24, 6, 40, 9.5, 'resultat', label=r'$P\cap Q=\{e\}$')
save(fig, '50-167')
