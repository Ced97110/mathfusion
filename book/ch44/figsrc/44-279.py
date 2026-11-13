import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
tab = [['b', 'c', 'a'], ['c', 'a', 'b'], ['a', 'b', 'c']]
c = 10.0; X, Y = 14.0, 22.0
for r in range(3):
    for k in range(3):
        role = 'resultat' if (r == 0 and tab[r][k] == 'b') else ('sujet' if r == 0 else 'fixe')
        box(ax, X + k * c, Y + (2 - r) * c, c, c, role, label=tab[r][k])
text(ax, X - 4, Y + 25, 'a', 'sujet', 'm', weight='bold')
text(ax, X + 5, Y + 36, 'x', 'resultat', 'm', weight='bold')
arrow(ax, (X + 5, Y + 34), (X + 5, Y + 30.8), 'resultat')
text(ax, 64, 50, r'$a\,x = b$', 'sujet', 'l', weight='bold')
text(ax, 64, 38, 'b : une seule fois\nsur la ligne de a', 'encre', 's')
box(ax, 8, 4, 72, 11, 'autre', label='neutre et inverses ?', size='m')
save(fig, '44-279')
