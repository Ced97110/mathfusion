import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cw, ch = 16.0, 9.0
x0 = 14
names = ['riz', 'lentilles', 'sel']
X = [2, 1, 4]; a = 3
assert [a * v for v in X] == [6, 3, 12]
for i in range(3):
    xc = x0 + i * (cw + 4)
    text(ax, xc + cw / 2, 58, names[i], 'fixe', 's')
    box(ax, xc, 42, cw, ch, 'sujet', label=str(X[i]))
    arrow(ax, (xc + cw / 2, 42), (xc + cw / 2, 21), 'varie', lw=1.0)
    text(ax, xc + cw / 2 + 1.5, 31.5, r'$\times 3$', 'varie', 's', ha='left')
    box(ax, xc, 9, cw, ch + 3, 'resultat', label=str(a * X[i]))
text(ax, 6, 46.5, r'$x$', 'sujet', 'l', weight='bold')
text(ax, 6, 14, r'$a x$', 'resultat', 'l', weight='bold')
text(ax, 44, 3, r'$a = 3$ pour chaque case', 'varie', 's')
save(fig, '58-036')
