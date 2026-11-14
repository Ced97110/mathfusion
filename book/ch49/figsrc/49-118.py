import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 2, 4, 84, 68, 'fixe', label=None)
text(ax, 44, 67.5, r'$G$ : les 8 éléments', 'fixe', 's')
box(ax, 5, 24, 78, 38, 'autre')
text(ax, 44, 57, r'commutent avec $r$ seul : 4', 'autre', 's')
box(ax, 8, 28, 36, 20, 'resultat')
text(ax, 26, 43.5, r'centre : 2', 'resultat', 's')
xs = [14, 32, 50, 68]
for x, n in zip(xs, ['1', r'$r^2$', r'$r$', r'$r^3$']):
    role = 'resultat' if n in ('1', r'$r^2$') else 'autre'
    disc(ax, x if role == 'autre' else x, 34, 4, role, label=n, size='s')
for x in xs:
    disc(ax, x, 17, 4, 'fixe', label=r'$s$' if False else None)
text(ax, 44, 19, 'réflexions : ne commutent pas avec r', 'fixe', 's') if False else text(ax, 44, 9, '4 réflexions', 'fixe', 's')
save(fig, '49-118')
