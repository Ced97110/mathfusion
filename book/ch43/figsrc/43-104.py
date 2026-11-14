import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
xs = [18, 44, 70]
text(ax, 44, 76, 'l’ensemble des trois pions', 'sujet', 's')
box(ax, 6, 48, 76, 20, 'sujet', fill=False); box(ax, 6, 14, 76, 20, 'autre', fill=False)
for x, a, n in zip(xs, 'ABC', '123'):
    disc(ax, x, 58, 4.5, 'sujet', label=r'$%s$' % a)
    disc(ax, x, 24, 4.5, 'autre', label=n)
    arrow(ax, (x, 53.2), (x, 28.8), 'varie')
text(ax, 48, 41, 'un pion, un numéro', 'varie', 's', ha='left')
text(ax, 44, 5, r'$|\{A,\ B,\ C\}| = 3$', 'resultat', 'l')
save(fig, '43-104')
