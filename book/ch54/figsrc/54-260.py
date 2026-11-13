import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 64, r'$x^2 + \,?\,x + \,?$ sur $\mathbb{Z}/2$', 'sujet', 's')
text(ax, 25, 55, 'constante 0', 'fixe', 's')
text(ax, 65, 55, 'constante 1', 'fixe', 's')
items = {(0, 0): (r'$x^2$', 'racine 0'), (0, 1): (r'$x^2+1$', 'racine 1'),
         (1, 0): (r'$x^2+x$', 'racines 0 et 1'), (1, 1): (r'$x^2+x+1$', 'aucune racine')}
for (a, c), (poly, rac) in items.items():
    role = 'resultat' if (a, c) == (1, 1) else 'fixe'
    x = 6 + c * 40
    y = 30 - a * 24
    box(ax, x, y, 36, 20, role)
    text(ax, x + 18, y + 14, poly, 'sujet', 's')
    text(ax, x + 18, y + 6, rac, role, 's')
text(ax, 44, 2, 'terme en x : 0 en haut, 1 en bas', 'fixe', 's')
save(fig, '54-260')
