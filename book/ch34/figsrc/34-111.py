import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def wedge(o, d, role):
    pts = [(o[0] + 14 * math.cos(math.radians(d * i / 30)), o[1] + 14 * math.sin(math.radians(d * i / 30))) for i in range(31)]
    poly(ax, [o] + pts, role); line(ax, [o, pts[0]], role, lw=1.2); line(ax, [o, pts[-1]], role, lw=1.2)
wedge((14, 53), 45, 'resultat'); wedge((54, 53), 90, 'limite')
line(ax, [(57, 53), (57, 56), (54, 56)], 'limite', lw=0.7)
cols = [(5, 'A = 45°', 'resultat', ['cos 90° = 0', '(1 − 0) / (1 + 0)', '= 1 = tan² 45°'], 'tan 45° existe'),
        (47, 'A = 90°', 'limite', ['cos 180° = −1', '(1 + 1) / (1 − 1)', '2 / 0 : impossible'], 'tan 90° n’existe pas')]
for x, head, r, labs, note in cols:
    text(ax, x + 19, 47.5, head, r, 's', weight='bold')
    for i, (y, l) in enumerate(zip([34, 22, 10], labs)):
        box(ax, x, y, 38, 9, r if i == 2 else 'fixe', label=l, size='s')
        if i < 2: arrow(ax, (x + 19, y), (x + 19, y - 3), 'varie')
    text(ax, x + 19, 4.5, note, r, 's')
save(fig, '34-111')
