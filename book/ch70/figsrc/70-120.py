import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, r'$f=y^2-1$ et $g=5$', 'encre', 'm')
f = numberline(ax, 14, 66, 58, -2, 2, 1, labels=False, arrow_right=True)
for v in (-1, 1):
    disc(ax, f(v), 58, 1.4, 'sujet')
text(ax, f(-1), 64, r'$-1$', 'sujet', 's')
text(ax, f(1), 64, r'$1$', 'sujet', 's')
text(ax, 44, 50, '$g=5$ : aucune racine', 'autre', 's')
for k, t in enumerate(['5', '0', '0', '5']):
    box(ax, 18 + 13 * (k % 2), 28 - 11 * (k // 2) + 6, 12, 9, 'autre', label=t)
text(ax, 54, 41, r'$5\times5-0\times0$', 'fixe', 's', ha='left')
box(ax, 44, 22, 34, 11, 'resultat', label=r'$\mathrm{Res}=25\neq0$', size='s')
save(fig, '70-120')
