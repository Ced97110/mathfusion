import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import gcd
fig, ax = canvas(60)
assert gcd(6, 10) == 2 and gcd(2, 0) == 2   # (6,10) = (2) : multiples de 2 ; (2, x) : 1 est PGCD de 2 et x
text(ax, 38, 55, 'PGCD', 'sujet', 'm', weight='bold')
text(ax, 69, 55, 'idéal engendré', 'autre', 'm', weight='bold')
text(ax, 2, 40, r'$\mathbb{Z}$' + '\n6 et 10', 'encre', 'm', ha='left')
box(ax, 30, 33, 16, 14, 'sujet', label='2', size='m')
text(ax, 50, 40, '=', 'resultat', 'xl', weight='bold')
box(ax, 54, 33, 32, 14, 'autre', label='multiples\nde 2', size='s')
text(ax, 2, 14, r'$\mathbb{Z}[x]$' + '\n2 et $x$', 'encre', 'm', ha='left')
box(ax, 30, 7, 16, 14, 'sujet', label='1', size='m')
text(ax, 50, 14, r'$\neq$', 'limite', 'xl', weight='bold')
box(ax, 54, 7, 32, 14, 'autre', label='ne contient\npas 1', size='s')
save(fig, '56-170')
