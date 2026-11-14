import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
data = [(r'$7$', r'$x$'), (r'$2$', r'$y$'), (r'$-8$', r'$z$')]
x = 5
for i, (c, l) in enumerate(data):
    box(ax, x, 28, 9.5, 11, 'sujet', label=c); box(ax, x + 10, 28, 7.5, 11, 'autre', label=l)
    x += 17.5 + 4.5
    text(ax, x - 2.25, 33.5, '+', 'varie', 'm')
box(ax, x, 28, 12, 11, 'fixe', label=r'$12$')
text(ax, x + 6, 22, 'aucune lettre', 'fixe', 's')
text(ax, 44, 50, 'les coefficients', 'sujet', 'm')
text(ax, 44, 9, r'$7$ ; $2$ ; $-8$', 'resultat', 'l')
arrow(ax, (44, 47), (44, 41), 'sujet')
save(fig, '15-031')
