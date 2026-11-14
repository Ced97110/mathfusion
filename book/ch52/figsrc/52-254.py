import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
mods = [95, 97, 98, 99]
data = [(38, '2134', 'sujet', [44, 0, 76, 55]), (20, '1531', 'autre', [11, 76, 61, 46])]
for i, m in enumerate(mods):
    text(ax, 24 + i * 16 + 7, 56, f'par {m}', 'encre', 's')
for y, n, role, rems in data:
    box(ax, 2, y, 18, 10, role, label=n, size='l', weight='bold')
    arrow(ax, (20.5, y + 5), (23.5, y + 5), 'varie')
    for i, r in enumerate(rems):
        box(ax, 24 + i * 16, y, 14, 10, role, label=str(r))
save(fig, '52-254')
