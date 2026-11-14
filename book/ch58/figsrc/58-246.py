import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 22, 72, r'$M_1=\mathbb{Z}^2$', 'sujet', 'm', weight='bold')
text(ax, 66, 72, r'$M_2=\mathbb{Z}^2$', 'autre', 'm', weight='bold')
rows = [(52, '(1, 0)', '(0, 0)'), (32, '(0, 0)', '(1, 0)')]
for y, a, b in rows:
    text(ax, 9, y + 5, '(1, 0) =', 'encre', 's')
    box(ax, 18, y, 26, 10, 'sujet', label=a, size='s')
    text(ax, 47, y + 5, '+', 'encre', 'l', weight='bold')
    box(ax, 50, y, 26, 10, 'autre', label=b, size='s')
text(ax, 44, 46, 'ou', 'fixe', 's')
box(ax, 6, 15, 76, 8, 'resultat', label='(i) vraie : tout est atteint', size='s')
box(ax, 6, 4, 76, 8, 'limite', label='(ii) fausse : 2 écritures', size='s')
save(fig, '58-246')
