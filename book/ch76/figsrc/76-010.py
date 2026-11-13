import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# gauche : nombres ordinaires, sans la règle
box(ax, 2, 6, 40, 72, 'autre', fill=False, lw=0.8, dash=True)
text(ax, 22, 72, 'sans la règle', 'autre', 'm'); text(ax, 22, 66, 'comme les nombres', 'autre', 's')
text(ax, 22, 50, r'$3\times 3=9$', 'autre', 'm'); text(ax, 22, 43, r'pas $0$', 'autre', 's')
text(ax, 22, 28, r'$2\times 3=3\times 2$', 'autre', 'm'); text(ax, 22, 21, 'aucun signe', 'autre', 's')
# droite : la règle
box(ax, 46, 6, 40, 72, 'sujet', fill=False, lw=0.8)
text(ax, 66, 72, 'avec la règle', 'sujet', 'm'); text(ax, 66, 66, 'flèches du plan', 'sujet', 's')
text(ax, 66, 54, r'$v\wedge v=0$', 'sujet', 'l')
arrow(ax, (50, 40), (72, 40), 'sujet', lw=1.2); text(ax, 61, 44, r'$v$', 'sujet', 'm')
arrow(ax, (50, 36), (72, 36), 'sujet', lw=1.2); text(ax, 61, 31, r'$v$', 'sujet', 'm')
text(ax, 66, 22, 'aire nulle', 'resultat', 'm')
save(fig, '76-010')
