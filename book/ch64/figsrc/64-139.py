import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
# départ : A5 est simple
box(ax, 24, 76, 40, 9, 'sujet', label=r'$A_5$ : 60 éléments')
text(ax, 44, 64, "$A_5$ simple, $A'_5$ normal :\n$A'_5=\\{e\\}$ ou $A'_5=A_5$", 'encre', 's')
arrow(ax, (34, 58), (19, 47), 'fixe')
arrow(ax, (54, 58), (66, 47), 'fixe')

# branche 1 : un seul élément
box(ax, 2, 36, 34, 10, 'limite', label=r"$A'_5=\{e\}$ : 1")
arrow(ax, (19, 35.5), (19, 28), 'limite')
text(ax, 19, 24, r'alors $A_5$ abélien', 'limite', 's')
text(ax, 19, 17, "or il ne l'est pas", 'limite', 's')
text(ax, 19, 10, 'impossible', 'limite', 's', weight='bold')
text(ax, 66, 8, 'impossible', 'limite', 's', weight='bold')
text(ax, 44, 3, r"donc $S_5$ n'est pas résoluble", 'resultat', 's')

# branche 2 : 60 éléments, la suite ne descend jamais
box(ax, 46, 36, 40, 10, 'limite', label=r"$A'_5=A_5$ : 60")
for k in range(3):
    x = 47 + 14 * k
    box(ax, x, 20, 9, 8, 'limite', label='60')
    if k < 2:
        arrow(ax, (x + 9.3, 24), (x + 13.7, 24), 'limite')
arrow(ax, (51.5, 35.5), (51.5, 28.5), 'limite')
text(ax, 66, 13, r"n'atteint jamais $\{e\}$", 'limite', 's')
save(fig, '64-139')
