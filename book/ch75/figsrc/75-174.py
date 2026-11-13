import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
ox, oy, u = 36, 36, 17
P = lambda a, b: (ox + a*u, oy + b*u)
for a in (-1, 0, 1):
    for b in (-1, 0, 1):
        on = abs(a) + abs(b) == 1
        disc(ax, *P(a, b), 2.6 if on else 1.4, 'sujet' if on else 'fixe')
lab = {(1, 0): '1', (-1, 0): '−1', (0, 1): '$i$', (0, -1): '$-i$'}
off = {(1, 0): (5.5, 0), (-1, 0): (-5.5, 0), (0, 1): (0, 5), (0, -1): (0, -5)}
for k, s in lab.items():
    text(ax, P(*k)[0]+off[k][0], P(*k)[1]+off[k][1], s, 'sujet', 'm', weight='bold')
text(ax, 72, 66, '9 éléments', 'fixe', 's'); text(ax, 72, 60, '$a+ib$', 'fixe', 's')
text(ax, 72, 46, r'$a\cdot a^{q}=1$', 'sujet', 'm', weight='bold')
text(ax, 72, 38, '$q$ = 3', 'sujet', 's')
text(ax, 72, 28, '$q+1$ = 4 points', 'resultat', 'm', weight='bold')
text(ax, 44, 4, 'les points bleus forment le « cercle »', 'sujet', 's')
save(fig, '75-174')
