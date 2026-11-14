import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
x = [2, 1, 4]
names = ['riz', 'lentilles', 'sel']
for k in range(3):
    xc = 12 + k * 26
    box(ax, xc, 40, 16, 9, 'varie', label=str(x[k]))
    text(ax, xc + 8, 54, r'$x_%d$' % (k + 1), 'varie', 's')
    line(ax, [(xc + 8, 40), (xc + 8, 29)], 'fixe', lw=0.8)
    text(ax, xc + 8, 34.5, '×', 'fixe', 'l')
    box(ax, xc, 20, 16, 9, 'sujet', label=r'$e_%d$' % (k + 1))
    text(ax, xc + 8, 15, names[k], 'sujet', 's')
    if k < 2: text(ax, xc + 21, 24.5, '+', 'encre', 'l', weight='bold')
box(ax, 8, 2, 72, 8, 'resultat', label=r'$\sum\, x_i\,e_i$ : 2 riz + 1 lentilles + 4 sel', size='s')
save(fig, '58-051')
