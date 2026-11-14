import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
text(ax, 44, 43, 'idéal engendré par 6 et 10', 'encre', 'm')
f = numberline(ax, 6, 72, 24, 0, 12, 1, every=2)
for v in range(0, 13, 2):
    role = {6: 'sujet', 10: 'sujet', 2: 'resultat'}.get(v, 'fixe')
    disc(ax, f(v), 31, 2.2, role)
text(ax, f(6), 36, '6', 'sujet', 's'); text(ax, f(10), 36, '10', 'sujet', 's')
text(ax, f(2), 36, 'PGCD 2', 'resultat', 's')
text(ax, 44, 8, 'les multiples de 2 (ronds) : restes par 2', 'resultat', 's')
save(fig, '52-292')
