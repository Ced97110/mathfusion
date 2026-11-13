import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 4, 38, 54, 20, 'sujet'); text(ax, 9, 54, r'$P$', 'sujet', 'm')
for x, n in ((12, 0), (24, 3), (36, 6), (48, 9)):
    disc(ax, x, 45, 4.5, 'resultat' if n == 3 else 'sujet', label=str(n), size='s')
disc(ax, 73, 45, 4.5, 'limite', label='4', size='s')
text(ax, 44, 31, r'$xPx^{-1}=P$ pour les deux', 'varie', 's')
box(ax, 3, 5, 40, 17, 'resultat'); box(ax, 47, 5, 39, 17, 'limite')
text(ax, 23, 17, r'$x=3$ : ordre $2^2$', 'resultat', 's'); text(ax, 23, 10, r'$x \in P$', 'resultat', 's', weight='bold')
text(ax, 66.5, 17, r'$x=4$ : ordre 3', 'limite', 's'); text(ax, 66.5, 10, r'$x \notin P$', 'limite', 's', weight='bold')
arrow(ax, (24, 22.5), (24, 40), 'resultat'); arrow(ax, (70, 22.5), (72.5, 40), 'limite')
save(fig, '50-111')
