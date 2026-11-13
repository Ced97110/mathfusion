import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs, ys, ps = [1, 2, 3], [4, 5, 6], ['4', '10', '18']
text(ax, 6, 54, r'$x$', 'sujet', 'm'); text(ax, 6, 44, r'$y$', 'autre', 'm')
for i in range(3):
    cx = 22 + i * 24
    box(ax, cx - 8, 38, 16, 22, 'fixe', fill=False)
    text(ax, cx, 54, str(xs[i]), 'sujet', 'm'); text(ax, cx, 44, str(ys[i]), 'autre', 'm')
    arrow(ax, (cx, 37), (cx, 29), 'varie')
    box(ax, cx - 8, 17, 16, 10, 'varie', label=ps[i])
brace(ax, 14, 78, 15, 'resultat', 'on additionne', True)
text(ax, 44, 4, r'$\langle x, y \rangle = 32$', 'resultat', 'l')
save(fig, '73-139')
