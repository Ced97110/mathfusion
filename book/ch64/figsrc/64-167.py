import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 20, 85, 'tour de corps', 'sujet', 'm', weight='bold')
text(ax, 68, 85, 'tour de groupes', 'autre', 'm', weight='bold')
ys = (10, 36, 62)
fields = (r'$\mathbb{Q}$', r'$\mathbb{Q}(j)$', r'$\mathbb{Q}(j,\sqrt[3]{2})$')
groups = ('6 éléments', '3 éléments', '1 élément')
for y, a, b in zip(ys, fields, groups):
    box(ax, 4, y, 32, 13, 'sujet', label=a)
    box(ax, 52, y, 32, 13, 'autre', label=b)
    arrow(ax, (37, y + 6.5), (51, y + 6.5), 'varie', both=True)
for i, d in enumerate(('2', '3')):
    ya, yb = ys[i] + 13, ys[i + 1]
    arrow(ax, (20, ya + 0.5), (20, yb - 0.5), 'sujet'); text(ax, 24, (ya + yb) / 2, d, 'sujet', 'm')
    arrow(ax, (68, ya + 0.5), (68, yb - 0.5), 'autre'); text(ax, 72, (ya + yb) / 2, d, 'autre', 'm')
save(fig, '64-167')
