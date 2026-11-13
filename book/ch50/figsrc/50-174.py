import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 59, r'$n_q\in\{1,\ p\}$ : $p=3$, $q=5$', 'encre', 'm')
for i in range(5):
    box(ax, 9 + 14 * i, 36, 13, 9, 'varie' if i < 2 else 'fixe', fill=i < 2)
text(ax, 9, 31.5, '0', 'fixe', 's'); text(ax, 79, 31.5, '5', 'fixe', 's')
brace(ax, 9, 36, 46, 'varie', label=r'$p-1=2$', down=False)
brace(ax, 9, 79, 29, 'fixe', label=r'$q=5$ cases : 0 et $q$ seuls multiples', down=True)
box(ax, 14, 4, 60, 9.5, 'resultat', label=r'$n_q=1$, le $q$-Sylow est normal', size='s')
save(fig, '50-174')
