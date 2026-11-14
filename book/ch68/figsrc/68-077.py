import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
x = '0111'
xs = [31 + 13 * i for i in range(4)]
text(ax, 20, 62, r'$H$', 'sujet', 'l', ha='right')
text(ax, 20, 44, r'$x$', 'autre', 'l', ha='right')
for i, cx in enumerate(xs):
    box(ax, cx - 5, 57, 10, 10, 'sujet', label='1')
    box(ax, cx - 5, 39, 10, 10, 'autre' if x[i] == '1' else 'fixe', label=x[i])
    if x[i] == '1':
        arrow(ax, (cx, 56.5), (cx, 50), 'varie')
    else:
        line(ax, [(cx, 56.5), (cx, 50)], 'fixe', dash=True)
text(ax, 50, 29, '1 + 1 + 1 = 1', 'encre', 'm')
text(ax, 50, 19, r'$Hx=1$', 'resultat', 'xl')
text(ax, 50, 8, r'$\neq 0$ : une erreur existe', 'resultat', 's')
save(fig, '68-077')
