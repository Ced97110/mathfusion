import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 4, 64, 80, 11, 'sujet', label=r'départ : 12 divise 8$m$', size='m')
arrow(ax, (44, 64), (44, 57), 'fixe')
box(ax, 4, 38, 80, 19, 'varie', label=r'on divise par $d$ = 4 :'+'\n'+r'12 $\rightarrow$ 3 et 8 $\rightarrow$ 2'+'\n'+r'donc 3 divise 2$m$', size='m', weight='bold')
arrow(ax, (44, 38), (44, 34), 'fixe')
box(ax, 4, 23, 80, 11, 'resultat', label=r'arrivée : le plus petit $m$ est 3', size='m')
text(ax, 44, 15.5, r'8$m$ est-il multiple de 12 ?', 'fixe', 's')
for i, (m, r_, role) in enumerate([(1, 8, 'limite'), (2, 16, 'limite'), (3, 24, 'resultat')]):
    box(ax, 4 + i * 28.5, 3, 25, 8, role, label=rf'$m$ = {m} : {r_}', size='s')
save(fig, '46-126')
