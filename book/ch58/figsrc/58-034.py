import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cw, ch = 16.0, 9.0
x0 = 14
names = ['riz', 'lentilles', 'sel']
X = [2, 1, 4]; Y = [1, 5, 3]
assert [a + b for a, b in zip(X, Y)] == [3, 6, 7]
for i in range(3):
    xc = x0 + i * (cw + 4)
    box(ax, xc - 2, 6, cw + 4, 47, 'fixe', fill=False, dash=True, lw=0.6)
    text(ax, xc + cw / 2, 57, names[i], 'fixe', 's')
    box(ax, xc, 40, cw, ch, 'sujet', label=str(X[i]))
    box(ax, xc, 24, cw, ch, 'autre', label=str(Y[i]))
    box(ax, xc, 8, cw, ch, 'resultat', label=str(X[i] + Y[i]))
    arrow(ax, (xc + cw / 2, 40), (xc + cw / 2, 34), 'varie', lw=0.9)
    arrow(ax, (xc + cw / 2, 24), (xc + cw / 2, 18), 'varie', lw=0.9)
text(ax, 6, 28.5, '+', 'varie', 'l', weight='bold')
text(ax, 6, 12.5, '=', 'resultat', 'l', weight='bold')
save(fig, '58-034')
