import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 5, 31, 38, 8, 'sujet')
for j in range(4):
    for i in range(5):
        disc(ax, 10 + 7 * i, 14 + 7 * j, 2.3, 'sujet' if j == 3 else 'fixe')
text(ax, 24, 44, '5-Sylow unique : normal', 'sujet', 's')
text(ax, 24, 6, r'$G$ : 20 = 4 × 5 éléments', 'fixe', 's')
text(ax, 67, 47, r'$n_5$ divise 4 : 1, 2 ou 4', 'encre', 's')
text(ax, 67, 38, 'restes par 5 : 1, 2, 4', 'encre', 's')
text(ax, 67, 29, 'seul 1 convient', 'resultat', 's')
box(ax, 48, 8, 38, 14, 'resultat', label=r'ni $\{e\}$ ni $G$ :' + '\npas simple', size='s')
save(fig, '50-222')
