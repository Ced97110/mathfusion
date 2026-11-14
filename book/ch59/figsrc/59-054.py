import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'ligne 2, avec la ligne 1 $=(4,\,6)$ fixe', 'encre', 's')
xs = [3, 35, 67]
for x, v, role in zip(xs, ['(6, 4)', '(18, 22)', '(6, 4)'], ['sujet', 'varie', 'resultat']):
    box(ax, x, 22, 18, 10, role, label=v)
arrow(ax, (22, 27), (34, 27), 'varie', lw=1.2)
text(ax, 28, 36, r'$T_{21}(3)$', 'varie', 's'); text(ax, 28, 21, '+ 3 × L1', 'varie', 's')
arrow(ax, (54, 27), (66, 27), 'autre', lw=1.2)
text(ax, 60, 36, r'$T_{21}(-3)$', 'autre', 's'); text(ax, 60, 21, '− 3 × L1', 'autre', 's')
text(ax, 12, 14, 'départ', 'sujet', 's'); text(ax, 76, 14, 'retrouvé', 'resultat', 's')
box(ax, 3, 3, 82, 6, 'fixe', label=r'ligne 1 : (4, 6), ne change pas', size='s')
save(fig, '59-054')
