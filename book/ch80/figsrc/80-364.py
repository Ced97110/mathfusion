import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
px = [38, 50, 62]
text(ax, 14, 84, r'$k$', 'encre', 'm'); text(ax, 77, 84, r'$T(k)$', 'resultat', 'm')
for x, p in zip(px, '235'): disc(ax, x, 84, 4, 'sujet', label=p)
for r, (k, ps, t) in enumerate([(6, '23', r'$\{2,3\}$'), (10, '25', r'$\{2,5\}$'), (7, '', r'$\varnothing$'), (30, '235', r'$\{2,3,5\}$')]):
    y = 64 - r * 16
    box(ax, 6, y - 5, 16, 10, 'fixe', label=str(k), size='l')
    for x, p in zip(px, '235'):
        if p in ps: disc(ax, x, y, 4, 'sujet')
        else: disc(ax, x, y, 4, 'fixe', fill=False)
    text(ax, 77, y, t, 'resultat', 'm')
text(ax, 44, 4, 'disque plein : le premier divise k', 'fixe', 's')
save(fig, '80-364')
