import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 40, 48, 'chaque disque = un 1 ajouté', 'fixe', 's')
text(ax, 83, 48, 'char', 'resultat', 's')
rows = [(40, r'$\mathbb{Z}/7$', 7, 7), (28, r'$\mathbb{Z}/6$', 6, 6), (16, r'$\mathbb{Z}$', 7, 0)]
for y, name, n, val in rows:
    text(ax, 9, y, name, 'sujet', 'm')
    for i in range(n):
        disc(ax, 22 + 6.5 * i, y, 2.2, 'sujet')
    xend = 22 + 6.5 * (n - 1)
    if val:
        text(ax, xend + 7, y, r'$=0$', 'resultat', 'm')
    else:
        text(ax, xend + 9, y, r'$\ldots\neq0$', 'limite', 'm')
    text(ax, 83, y, str(val), 'resultat', 'l', weight='bold')
save(fig, '51-131')
