import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
line(ax, [(44, 8), (44, 72)], 'fixe', lw=0.6, dash=True)
# à gauche : -1 sur un nombre
text(ax, 22, 72, 'sur un nombre', 'autre', 'm', weight='bold')
box(ax, 8, 54, 28, 12, 'autre', label=r'$5^{-1}$', size='xl')
arrow(ax, (22, 54), (22, 44), 'autre')
box(ax, 4, 30, 36, 13, 'autre', label='un divisé par 5')
text(ax, 22, 22, 'inverse de 5', 'autre', 's')
# à droite : -1 sur une fonction
text(ax, 66, 72, 'sur une fonction', 'sujet', 'm', weight='bold')
box(ax, 52, 54, 28, 12, 'sujet', label=r'$f^{-1}$', size='xl')
arrow(ax, (66, 54), (66, 44), 'sujet')
box(ax, 48, 30, 36, 13, 'sujet', label='réciproque de $f$')
box(ax, 48, 14, 36, 11, 'resultat', label=r'$f^{-1}(14)=11$')
text(ax, 66, 6, r'pas 1 ÷ $f(14)$ = 1 ÷ 17', 'limite', 's')
save(fig, '53-040')
