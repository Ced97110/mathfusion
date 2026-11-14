import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cx, cy = 58, 32
radii = [26, 21, 16, 11, 6]
labs = ['(3)', '(6)', '(12)', '(24)', '(48)']
for r in radii:
    disc(ax, cx, cy, r, 'sujet')
for r, l in zip(radii, labs):
    text(ax, cx, cy + r - 2.6, l, 'sujet', 's')
arrow(ax, (cx, cy - 3), (cx + 24, cy - 3), 'varie')
text(ax, cx + 13, cy - 8, 'plus grands', 'varie', 's')
text(ax, 58, 63, 'idéaux', 'sujet', 'm', weight='bold')
text(ax, 11, 63, 'diviseurs', 'sujet', 'm', weight='bold')
for i, n in enumerate(['48', '24', '12', '6', '3']):
    text(ax, 11, 53 - i * 10, n, 'sujet', 'm')
arrow(ax, (22, 56), (22, 8), 'varie')
text(ax, 18, 32, 'plus petits', 'varie', 's', rot=90)
save(fig, '56-086')
