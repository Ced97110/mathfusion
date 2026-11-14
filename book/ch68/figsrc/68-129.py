import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(64)
f = numberline(ax, 8, 78, 16, 0, 7, labels=False, arrow_right=False)
text(ax, 44, 59, r'16 mots = 1 + 7 + 7 + 1', 'sujet', 'l', weight='bold')
for v, n, role in ((0, 1, 'fixe'), (3, 7, 'resultat'), (4, 7, 'sujet'), (7, 1, 'sujet')):
    for i in range(n):
        cell(ax, f(v), 18.5 + i * 2.8 + 1.4, 8, 2.6, role)
    text(ax, f(v), 18.5 + n * 2.8 + 2.6, str(n), role, 'm', weight='bold')
    text(ax, f(v), 11.5, str(v), role, 'm')
text(ax, 44, 5, 'poids du mot (nombre de 1)', 'fixe', 's')
text(ax, 21, 28, r'$d = 3$', 'resultat', 'l', weight='bold')
arrow(ax, (27, 28), (33, 28), 'resultat')
save(fig, '68-129')
