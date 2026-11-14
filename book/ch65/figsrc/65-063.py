import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
box(ax, 20, 66, 48, 11, 'sujet', label=r'$d$ est-il un carré dans $F$ ?', size='s')
arrow(ax, (34, 65.5), (22, 55), 'fixe', lw=0.9)
arrow(ax, (54, 65.5), (66, 55), 'fixe', lw=0.9)
text(ax, 22, 59, 'non', 'limite', 's', weight='bold') if False else None
text(ax, 21, 61.5, 'non', 'varie', 's', weight='bold')
text(ax, 67, 61.5, 'oui', 'resultat', 's', weight='bold')
# left : S2
box(ax, 2, 14, 41, 40, 'varie', fill=False)
disc(ax, 12, 40, 4.4, 'sujet', label=r'$r_1$', size='s')
disc(ax, 33, 40, 4.4, 'sujet', label=r'$r_2$', size='s')
arrow(ax, (17, 40), (28, 40), 'varie', lw=1.2, both=True)
text(ax, 22.5, 31, 'l’échange est dans G', 'varie', 's')
text(ax, 22.5, 22, r'$G=S_2$', 'varie', 'm', weight='bold')
text(ax, 22.5, 16.5, '2 éléments', 'varie', 's')
# right : A2
box(ax, 45, 14, 41, 40, 'resultat', fill=False)
disc(ax, 55, 40, 4.4, 'sujet', label=r'$r_1$', size='s')
disc(ax, 76, 40, 4.4, 'sujet', label=r'$r_2$', size='s')
text(ax, 65.5, 31, 'aucun échange', 'resultat', 's')
text(ax, 65.5, 22, r'$G=A_2=\{1\}$', 'resultat', 'm', weight='bold')
text(ax, 65.5, 16.5, '1 élément', 'resultat', 's')
text(ax, 44, 7, 'il n’y a pas d’autre cas', 'fixe', 's')
save(fig, '65-063')
