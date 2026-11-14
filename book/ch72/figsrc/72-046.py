import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
def ax2(cx, cy, r):
    arrow(ax, (cx - r, cy), (cx + r, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - r), (cx, cy + r), 'fixe', lw=0.6)
line(ax, [(44, 6), (44, 76)], 'fixe', lw=0.6, dash=True)
# left : dimension 1
text(ax, 23, 75, 'dimension 1', 'sujet', 'm', weight='bold')
arrow(ax, (6, 58), (38, 58), 'sujet', lw=1.6)
# right : dimension 2
text(ax, 65, 75, 'dimension 2', 'resultat', 'm', weight='bold')
ax2(65, 58, 12)
line(ax, [(55, 49), (75, 67)], 'limite', lw=1.6)
text(ax, 74, 47, '(1, 1)', 'limite', 's')
rows = [('dimension 2', False, True), ('non dégénéré', True, True), ('vecteur isotrope', False, True)]
for k, (l, a, b) in enumerate(rows):
    y = 38 - k * 8
    for cx, ok in ((23, a), (65, b)):
        text(ax, cx, y, ('✓ ' if ok else '✗ ') + l, 'resultat' if ok else 'limite', 's')
box(ax, 4, 3, 38, 10, 'limite', label='pas un plan hyperbolique', size='s')
box(ax, 46, 3, 38, 10, 'resultat', label='plan hyperbolique', size='s', weight='bold')
save(fig, '72-046')
