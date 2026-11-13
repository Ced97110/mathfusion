import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 14, 56, 60, 10, 'autre', label='Jacobson a vérifié, en général :', size='s')
names = ['bien défini', 'commutatif', 'associatif', 'distributif']
xs = [2.25 + i * 21.5 for i in range(4)]
for i, n in enumerate(names):
    box(ax, xs[i], 36, 19, 11, 'sujet')
    text(ax, xs[i] + 9.5, 43, n, 'sujet', 's')
    text(ax, xs[i] + 9.5, 39, '✓ vérifié', 'resultat', 's')
    arrow(ax, (44, 56), (xs[i] + 9.5, 47.5), 'autre')
# the example is only a trace of one property
line(ax, [(xs[1] + 9.5, 36), (xs[1] + 9.5, 29)], 'fixe', dash=True)
text(ax, 44, 25, 'une trace de la commutativité,', 'fixe', 's')
text(ax, 44, 21, 'sur deux couples seulement :', 'fixe', 's')
text(ax, 44, 12, r'$(3,1)\times(2,5)=(11,17)$', 'resultat', 's')
text(ax, 44, 6, r'$(2,5)\times(3,1)=(11,17)$', 'resultat', 's')
save(fig, '13-114')
