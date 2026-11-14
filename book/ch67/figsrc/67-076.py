import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'racines de $x^3-x$ : $u^3=u$, corps à 3 éléments', 'sujet', 's')
rows = [('1', r'opposé $-u=2$', '$2^3=8=2$\nracine'), ('2', r'inverse $u^{-1}=2$', '$2^3=2$\nracine')]
for k, (u, mid, end) in enumerate(rows):
    y = 34 - k * 24
    box(ax, 2, y, 18, 12, 'sujet', label=rf'$u = {u}$', size='s')
    arrow(ax, (21, y + 6), (25, y + 6), 'varie')
    box(ax, 26, y, 32, 12, 'autre', label=mid, size='s')
    arrow(ax, (59, y + 6), (63, y + 6), 'varie')
    box(ax, 64, y, 22, 12, 'resultat', label=end, size='s')
text(ax, 44, 7, 'opposé et inverse : encore des racines', 'resultat', 's')
save(fig, '67-076')
