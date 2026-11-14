import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, '8 éléments', 'fixe', 's')
names = [('1', '−1'), ('I', '−I'), ('J', '−J'), ('K', '−K')]
for i, (p, n) in enumerate(names):
    x = 6 + i * 20
    fp = p if p == '1' else r'$%s$' % p
    fn = n if n == '−1' else r'$-%s$' % n[1]
    box(ax, x, 57, 16, 9, 'sujet', label=fp)
    box(ax, x, 45, 16, 9, 'autre', label=fn)
box(ax, 6, 29, 76, 11, 'resultat', label=r'$I^2 = J^2 = K^2 = -1$')
text(ax, 44, 22, 'l’ordre compte', 'limite', 'm')
box(ax, 4, 4, 32, 12, 'sujet', label=r'$IJ = K$')
box(ax, 52, 4, 32, 12, 'autre', label=r'$JI = -K$')
text(ax, 44, 10, r'$\neq$', 'limite', 'l')
save(fig, '44-198')
