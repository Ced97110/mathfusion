import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 50, 50, '1 ligne = 1 équation', 'fixe', 's')
text(ax, 19, 39, r'$H=$', 'sujet', 'm', ha='right')
xs = [27.5 + 14 * i for i in range(4)]
for i, cx in enumerate(xs):
    box(ax, cx - 5.5, 34, 11, 10, 'sujet', label='1')
    line(ax, [(cx, 33), (cx, 21)], 'fixe')
    text(ax, cx, 17, rf'$x_{i + 1}$', 'encre', 'm')
brace(ax, xs[0], xs[-1], 11, 'resultat', label='somme = 0', down=True)
save(fig, '68-076')
