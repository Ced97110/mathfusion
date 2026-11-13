import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 38, 76, 'Sym', 'sujet', 14, weight='bold')
text(ax, 51, 76, r'$S$', 'varie', 14, weight='bold')
text(ax, 44, 63, 'désigne tout cet ensemble :', 'encre', 's')
box(ax, 4, 6, 80, 50, 'sujet')
text(ax, 44, 48, r'les transformations de $S$', 'sujet', 's', weight='bold')
text(ax, 44, 42, 'qui se défont', 'sujet', 's')
perms = [(0, 1, 2), (1, 0, 2), (1, 2, 0)]
for cx, p in zip([18, 44, 70], perms):
    xl, xr = cx - 6, cx + 6
    ys = [32, 25, 18]
    for i in range(3):
        line(ax, [(xl, ys[i]), (xr, ys[p[i]])], 'sujet', lw=1.0)
    for i in range(3):
        disc(ax, xl, ys[i], 1.7, 'varie'); disc(ax, xr, ys[i], 1.7, 'varie')
text(ax, 44, 9.5, 'chaque point arrive une fois', 'fixe', 's')
save(fig, '44-117')
