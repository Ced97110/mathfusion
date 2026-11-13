import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 18, 62, r'$c+d\,u$', 'encre', 'm', ha='left'); text(ax, 84, 62, r'$2^2=4$ éléments', 'resultat', 'm', ha='right')
for (c, d, role, lab) in [(0, 0, 'fixe', '0'), (1, 0, 'sujet', '1'), (0, 1, 'varie', r'$u$'), (1, 1, 'resultat', r'$1+u$')]:
    box(ax, 18 + 26 * c, 14 + 20 * d, 26, 20, role, label=lab, size='l')
for c in (0, 1): text(ax, 31 + 26 * c, 9, f'c = {c}', 'encre', 's')
for d in (0, 1): text(ax, 16, 24 + 20 * d, f'd = {d}', 'encre', 's', ha='right')
save(fig, '61-235')
