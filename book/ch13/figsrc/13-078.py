import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y = 38
f = numberline(ax, 6, 78, y, -3.5, 3.5, labels=False)
for v, r in ((-2, 'varie'), (0, 'fixe'), (2, 'sujet')):
    text(ax, f(v), y - 3.6, f'${v}$', r)
disc(ax, f(2), y, 1.8, 'sujet')
disc(ax, f(-2), y, 1.8, 'varie')
arrow(ax, (f(2) - 1, y + 3), (f(-2) + 1, y + 3), 'varie', curve=0.4)
text(ax, f(0), y + 14.5, r'$\times(-1)$ : 1er retournement', 'varie', 's')
arrow(ax, (f(-2) + 1, y - 7), (f(2) - 1, y - 7), 'varie', curve=0.4)
text(ax, f(0), y - 20, r'$\times(-1)$ : 2e retournement', 'varie', 's')
text(ax, 44, 4, r'retour sur $2$ : $(-1)\times(-1)=1$', 'resultat', 's')
save(fig, '13-078')
