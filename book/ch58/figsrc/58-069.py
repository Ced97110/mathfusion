import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
box(ax, 2, 78, 40, 12, 'sujet', label=r'$f_j=\sum a_{ji}\,e_i$')
box(ax, 46, 78, 40, 12, 'autre', label=r'$e_i=\sum b_{ij}\,f_j$')
arrow(ax, (42, 84), (46, 84), 'varie', both=True)
text(ax, 44, 72, 'substituer : $e_i$ avec des $e_i$', 'varie', 's')
text(ax, 44, 65, 'un lot (3, 1) pour 2 sacs', 'encre', 'm')
steps = [(53, 'sujet', '? × (3, 1) = (1, 0)'), (37, 'varie', '2e case : ? × 1 = 0 → ? = 0'),
         (21, 'limite', '1re case : 0 × 3 = 0, pas 1')]
for y, role, lab in steps:
    box(ax, 9, y - 5, 70, 10, role, label=lab, size='m')
for y in (48, 32):
    arrow(ax, (44, y), (44, y - 6), 'fixe')
save(fig, '58-069')
