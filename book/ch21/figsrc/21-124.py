import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
f = numberline(ax, 10, 70, 52, -1, 5, 1, labels=False)
for v, r in ((0, 'limite'), (1, 'limite'), (4, 'resultat')):
    disc(ax, f(v), 52, 1.8, r)
    text(ax, f(v), 46.5, f'{v}', r, 's')
text(ax, (f(0) + f(1)) / 2, 59, 'interdites', 'limite', 's')
text(ax, f(4), 59, 'candidat', 'resultat', 's')
text(ax, 15, 36, 'côté gauche', 'sujet', 's'); text(ax, 73, 36, 'côté droit', 'autre', 's')
box(ax, 2, 18, 30, 13, 'sujet', label=r'$\frac{73}{12}$', size='m')
text(ax, 44, 24.5, '=', 'resultat', 'l')
box(ax, 56, 18, 30, 13, 'autre', label=r'$\frac{73}{12}$', size='m')
text(ax, 44, 8, 'pour $x=4$ : égaux', 'resultat', 's')
save(fig, '21-124')
