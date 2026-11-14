import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import gcd
fig, ax = canvas(72)
assert gcd(gcd(4, 6), 10) == 2 and gcd(gcd(2, 3), 5) == 1
text(ax, 2, 68, 'existence', 'sujet', 'm', ha='left', weight='bold')
box(ax, 2, 49, 30, 12, 'sujet', label=r'$4x^2+6x+10$', size='s')
text(ax, 36, 55, '=', 'fixe', 'm')
box(ax, 40, 49, 10, 12, 'varie', label='2', size='m')
text(ax, 54, 55, r'$\times$', 'fixe', 'm')
box(ax, 58, 49, 28, 12, 'fixe', label=r'$2x^2+3x+5$', size='s')
text(ax, 45, 44, 'contenu', 'varie', 's')
text(ax, 72, 44, 'primitif : on le casse', 'fixe', 's')
text(ax, 2, 34, r'unicité : $u$, $v$ primitifs associés', 'autre', 'm', ha='left', weight='bold')
box(ax, 2, 6, 23, 16, 'autre', label=r'$u=\frac{a}{b}v$' + '\n$a/b$ réduite', size='s')
box(ax, 32, 6, 23, 16, 'autre', label=r'$bu=av$' + '\ncontenus $b$, $a$', size='s')
box(ax, 62, 6, 24, 16, 'resultat', label=r'$a,b$ unités' + '\n$u$, $v$ associés' + '\ndans $D[x]$', size='s')
arrow(ax, (25.5, 14), (31.5, 14), 'varie'); text(ax, 28.5, 25.5, r'$\times b$', 'varie', 's')
arrow(ax, (55.5, 14), (61.5, 14), 'varie'); text(ax, 58.5, 25.5, '=', 'varie', 's')
save(fig, '56-157')
