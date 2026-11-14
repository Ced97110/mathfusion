import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
box(ax, 4, 66, 80, 16, 'sujet', label=r'départ : $\eta$ et $\theta$' + '\n' + 'même permutation des racines', size='s')
arrow(ax, (44, 66), (44, 56), 'varie')
box(ax, 4, 34, 80, 22, 'varie', label=r'$E$ est engendré par les racines' + '\n' + r'donc $\eta$ et $\theta$ agissent pareil' + '\n' + 'sur $F$ et sur $r_1,\\dots,r_n$', size='s', weight='bold')
text(ax, 44, 28, r'$\eta(a+b\sqrt{2})=a+b\,\eta(\sqrt{2})$ : tout se déduit', 'varie', 's')
arrow(ax, (44, 23), (44, 16.5), 'varie')
box(ax, 4, 4, 80, 12, 'resultat', label=r'arrivée : $\eta=\theta$ sur tout $E$', size='s')
save(fig, '65-026')
