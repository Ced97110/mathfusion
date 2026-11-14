import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r"si $H$ sort de $P'$", 'encre', 'm')
X = lambda j: 10 + 6 * j
text(ax, 4, 59, r"$P'$ : 4 éléments", 'sujet', 's', ha='left')
for j in range(4): disc(ax, X(j), 53, 2.4, 'sujet')
text(ax, 4, 43, r"$HP'$ : puissance de 2, 8 ou plus", 'varie', 's', ha='left')
for j in range(8): disc(ax, X(j), 37, 2.4, 'sujet' if j < 4 else 'varie')
text(ax, 4, 27, r'$|G| = 12$ éléments', 'fixe', 's', ha='left')
for j in range(12): disc(ax, X(j), 21, 2.4, 'fixe')
text(ax, 44, 11, '8 ne divise pas 12', 'limite', 'm', weight='bold')
text(ax, 44, 5, r"impossible : $P'$ est maximal", 'limite', 's')
save(fig, '50-102')
