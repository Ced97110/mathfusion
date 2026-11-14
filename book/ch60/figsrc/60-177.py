import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# haut : la preuve, courte
box(ax, 14, 72, 60, 10, 'resultat', label=r'$f(A)=0$ : preuve en une ligne', size='s')
arrow(ax, (44, 55), (44, 71), 'varie')
# milieu : l'étape qui porte le poids
box(ax, 14, 42, 60, 12, 'varie', label=r'produit des facteurs $=f$', size='s')
arrow(ax, (44, 30), (44, 41), 'varie')
text(ax, 62, 60, 'on lit', 'varie', 's', ha='left')
# bas : la forme normale
box(ax, 4, 2, 80, 28, 'sujet')
text(ax, 44, 25, 'forme normale (ch. 59)', 'sujet', 'm', weight='bold')
text(ax, 44, 17, r'$P(\lambda1-A)Q=\mathrm{diag}(1,(\lambda-2)^2)$', 'sujet', 's')
text(ax, 44, 8, r'chaîne de facteurs : $1$, $(\lambda-2)^2$', 'sujet', 's')
save(fig, '60-177')
