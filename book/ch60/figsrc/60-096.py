import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
xs = [4, 34, 64]
rows = [(48, ['A B C', 'B A C', 'B C A'], "d'abord 1-2, puis 2-3"),
        (14, ['A B C', 'A C B', 'C A B'], "d'abord 2-3, puis 1-2")]
for y, labs, cap in rows:
    text(ax, 4, y + 15, cap, 'varie', 's', ha='left')
    for i, (x, v) in enumerate(zip(xs, labs)):
        box(ax, x, y, 20, 10, 'sujet' if i < 2 else 'varie', label=v)
    arrow(ax, (24, y + 5), (34, y + 5), 'varie')
    arrow(ax, (54, y + 5), (64, y + 5), 'varie')
text(ax, 74, 36, '≠', 'limite', 'xl', weight='bold')
save(fig, '60-096')
