import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from math import gcd
fig, ax = canvas(74)
rows = [(52, r'$f$', [2, 4], 'sujet'), (36, r'$g$', [3, 6], 'autre'), (18, r'$fg$', [6, 24, 24], 'resultat')]
for y, lab, co, role in rows:
    text(ax, 6, y + 4.5, lab, role, 'l')
    for i, v in enumerate(co):
        box(ax, 14 + i * 14, y, 12, 9, role, label=str(v), size='m')
    d = gcd(*co)
    text(ax, 60, y + 4.5, f'contenu {d}', role, 'm', ha='left')
assert gcd(6, 24, 24) == 6 == 2 * 3
text(ax, 44, 6, r'$2\times3=6$ : le contenu se multiplie', 'resultat', 's')
text(ax, 44, 68, r'$(2x+4)(3x+6)=6x^2+24x+24$', 'encre', 's')
save(fig, '56-153')
