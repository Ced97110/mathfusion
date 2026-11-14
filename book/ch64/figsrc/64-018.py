import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 74, r'$V$ : 4 permutations', 'sujet', 'm', weight='bold')
cx = [34, 48, 62, 76]
for k in range(4):
    text(ax, cx[k], 65, str(k + 1), 'fixe', 'm')
rows = [('e', []),
        ('(12)(34)', [(0, 1, -1.0), (2, 3, -1.0)]),
        ('(13)(24)', [(0, 2, -0.36), (1, 3, 0.36)]),
        ('(14)(23)', [(0, 3, 0.22), (1, 2, -1.0)])]
for i, (name, arcs) in enumerate(rows):
    y = 54 - 16 * i
    text(ax, 2, y, name, 'sujet', 's', ha='left')
    for k in range(4): disc(ax, cx[k], y, 2.6, 'sujet')
    for a, b, cur in arcs:
        arrow(ax, (cx[a] + 2.9, y), (cx[b] - 2.9, y), 'varie', curve=cur, both=True)
save(fig, '64-018')
