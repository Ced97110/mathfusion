import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
b, q, a = 2 + 1j, 3 - 1j, 7 + 2j
assert b * q == 7 + 1j and a - b * q == 1j and 6 - 2j + 3j + 1 == 7 + 1j
xs = [3, 33, 63]
text(ax, 3, 75, '1. multiplier', 'varie', 's', ha='left', weight='bold')
for x, lab, role in zip(xs, [r'$b=2+i$', r'$q=3-i$', r'$bq=7+i$'], ['sujet', 'varie', 'fixe']):
    box(ax, x, 60, 22, 12, role, label=lab, size='s')
text(ax, 29, 66, r'$\times$', 'fixe', 'm'); text(ax, 59, 66, '=', 'fixe', 'm')
text(ax, 44, 53, r'$(2+i)(3-i)=6-2i+3i+1=7+i$', 'fixe', 's')
text(ax, 3, 41, '2. soustraire', 'varie', 's', ha='left', weight='bold')
for x, lab, role in zip(xs, [r'$a=7+2i$', r'$bq=7+i$', r'$r=i$'], ['autre', 'fixe', 'resultat']):
    box(ax, x, 26, 22, 12, role, label=lab, size='s')
text(ax, 29, 32, r'$-$', 'fixe', 'm'); text(ax, 59, 32, '=', 'fixe', 'm')
text(ax, 44, 19, r'$(7+2i)-(7+i)=i$', 'fixe', 's')
text(ax, 44, 9, r'taille de $r$ : $1$ ; de $b$ : $5$', 'resultat', 's')
save(fig, '56-178')
