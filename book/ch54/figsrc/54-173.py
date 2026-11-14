import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
# dans Z : (4, 6) = (2)
text(ax, 44, 83, r'dans $\mathbb{Z}$ : engendré par $4$ et $6$', 'sujet', 'm')
f = numberline(ax, 6, 76, 68, -6, 6, step=1, every=2, arrow_right=False)
for v in range(-6, 7, 2):
    disc(ax, f(v), 68, 1.5, 'sujet')
text(ax, 44, 57, r'tous les multiples de $2$', 'sujet', 's')
box(ax, 22, 40, 44, 10, 'resultat', label='un seul générateur : 2', size='s')
text(ax, 44, 34, 'idéal principal', 'resultat', 's')
# dans Z[x]
text(ax, 44, 23, r'dans $\mathbb{Z}[x]$ : $x^3-2x^2+4$ et $x-1$', 'autre', 's')
text(ax, 44, 14, r'contient $3$, pas $1$', 'autre', 's')
text(ax, 44, 5, 'pas un seul générateur', 'limite', 's')
save(fig, '54-173')
