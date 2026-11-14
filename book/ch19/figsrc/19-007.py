import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
for x0, role, a, b in [(3, 'sujet', 2, 5), (50, 'autre', 5, 2)]:
    text(ax, x0 + 17.5, 40, f'({a}, {b})', role, 'l')
    box(ax, x0, 18, 17, 14, role, label=str(a), size='xl'); box(ax, x0 + 18, 18, 17, 14, role, label=str(b), size='xl')
    text(ax, x0 + 8.5, 12, '1re place', 'fixe', 's'); text(ax, x0 + 26.5, 12, '2e place', 'fixe', 's')
text(ax, 44, 25, r'$\neq$', 'limite', 'xl')
text(ax, 44, 3, 'l’ordre fait partie du couple', 'encre', 's')
save(fig, '19-007')
