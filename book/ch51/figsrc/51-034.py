import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def row(y, grp, lab):
    xs = [8, 30, 52]
    if grp == 0: box(ax, 5, y - 2, 37, 14, 'fixe', fill=False, dash=True)
    else: box(ax, 27, y - 2, 40, 14, 'fixe', fill=False, dash=True)
    for x, s in zip(xs, 'abc'): box(ax, x, y, 10, 10, 'sujet', label=f'${s}$')
    text(ax, 24, y + 5, '+', 'encre'); text(ax, 46, y + 5, '+', 'encre')
    text(ax, 78, y + 5, lab, 'fixe', 's')
row(46, 0, 'd’abord a + b'); row(22, 1, 'd’abord b + c')
for y in (46, 22):
    pass
box(ax, 22, 2, 44, 9, 'resultat', label='même somme', size='m')
arrow(ax, (30, 21), (40, 12.5), 'resultat'); arrow(ax, (58, 21), (48, 12.5), 'resultat')
save(fig, '51-034')
