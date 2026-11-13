import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 14, 44, 24, 11, 'sujet', label=r'$x=2$'); box(ax, 50, 44, 24, 11, 'sujet', label=r'$y=3$')
text(ax, 44, 60, r'$(x,y)$', 'sujet', 'm')
arrow(ax, (26, 43), (26, 27), 'fixe'); arrow(ax, (62, 43), (62, 27), 'varie')
text(ax, 24, 35, 'conjugué', 'fixe', 's', ha='right'); text(ax, 64, 35, 'signe changé', 'varie', 's', ha='left')
box(ax, 14, 15, 24, 11, 'fixe', label=r'$\bar{x}=2$'); box(ax, 50, 15, 24, 11, 'varie', label=r'$-y=-3$')
text(ax, 44, 8, r'$\mathrm{conj}(x,y)=(\bar{x},-y)$', 'resultat', 'm')
save(fig, '78-093')
