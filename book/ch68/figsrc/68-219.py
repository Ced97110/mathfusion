import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'tableau 2 × 2 : son déterminant', 'encre', 'm', weight='bold')
for (r, c), v, role in [((0, 0), '1', 'fixe'), ((0, 1), '1', 'fixe'), ((1, 0), '2', 'varie'), ((1, 1), '5', 'varie')]:
    box(ax, 8 + c * 14, 44 - r * 11, 12, 9, role, label=v, size='l')
for xb, d in ((6, 1), (36, -1)):
    line(ax, [(xb + d * 1.5, 55), (xb, 55), (xb, 31), (xb + d * 1.5, 31)], 'fixe', lw=0.9)
text(ax, 44, 50, r'$1 \times 5 = 5$', 'encre', 'm', ha='left')
text(ax, 44, 41, r'$1 \times 2 = 2$', 'encre', 'm', ha='left')
text(ax, 44, 32, r'$5 - 2 = 3$', 'resultat', 'l', ha='left', weight='bold')
text(ax, 44, 23, r'avec $s$ colonnes : puissances de $\omega$', 'sujet', 's')
for i, s in enumerate([r'$\omega$', r'$\omega^2$', r'$\cdots$', r'$\omega^s$']):
    box(ax, 7.5 + i * 19, 10, 16, 8, 'sujet', label=s, size='m')
text(ax, 44, 4, 'son déterminant : chapitre 76', 'fixe', 's')
save(fig, '68-219')
