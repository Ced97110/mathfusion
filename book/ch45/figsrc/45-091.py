import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$G_L$ est un groupe', 'sujet', 'l')
box(ax, 2, 40, 24, 11, 'fixe', label='neutre'); box(ax, 30, 40, 56, 11, 'resultat', label=r'$1_L \in G_L$ (identité)')
box(ax, 2, 25, 24, 11, 'fixe', label='stable'); box(ax, 30, 25, 56, 11, 'resultat', label=r'+1 puis +2 = +3, dans $G_L$')
box(ax, 2, 4, 24, 17, 'varie', label='inverse'); box(ax, 30, 4, 56, 17, 'varie')
text(ax, 58, 15.5, r'$a_L\circ(a^{-1})_L=1_L$', 'varie', 'm')
text(ax, 58, 9, '+1 puis +3 = +0', 'varie', 's')
save(fig, '45-091')
