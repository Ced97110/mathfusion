import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, 'toute valeur de $x$ convient', 'resultat', 'm', weight='bold')
f = numberline(ax, 12, 72, 22, 0, 10, 2, arrow_right=False)
arrow(ax, (4, 22), (84, 22), 'resultat', lw=2.4, both=True)
for v in (2, 10):
    disc(ax, f(v), 22, 1.8, 'resultat')
    box(ax, f(v) - 12, 33, 24, 9, 'resultat', label='12 = 12', size='s')
    arrow(ax, (f(v), 33), (f(v), 24.5), 'resultat')
text(ax, 44, 6, 'rien ne limite $x$', 'fixe', 's')
save(fig, '16-126')
