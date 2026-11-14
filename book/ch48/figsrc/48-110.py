import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
P = {'HN': (44, 58, 'sujet', r'$HN$ : 6'), 'H': (22, 36, 'sujet', r'$H$ : 3'), 'N': (66, 36, 'autre', r'$N$ : 2'), 'I': (44, 14, 'fixe', r'$H\cap N$ : 1')}
for a, b, r in [('I', 'H', 'resultat'), ('I', 'N', 'fixe'), ('H', 'HN', 'fixe'), ('N', 'HN', 'resultat')]:
    line(ax, [(P[a][0], P[a][1] + 4), (P[b][0], P[b][1] - 4)], r, lw=1.6 if r == 'resultat' else 1.0)
for x, y, r, s in P.values():
    box(ax, x - 12, y - 4, 24, 8, r, label=s, size='s')
text(ax, 12, 22, '3 paquets', 'resultat', 's'); text(ax, 76, 50, '3 paquets', 'resultat', 's')
text(ax, 44, 3, r'$HN/N\ \cong\ H/(H\cap N)$', 'resultat', 's')
save(fig, '48-110')
