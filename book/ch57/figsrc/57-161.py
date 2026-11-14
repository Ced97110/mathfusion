import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 60, 'ℤ, groupe', 'sujet', 'm', weight='bold')
text(ax, 66, 60, 'R, module sur R', 'autre', 'm', weight='bold')
disc(ax, 22, 48, 4.2, 'sujet', label='1', size='l')
disc(ax, 66, 48, 4.2, 'autre', label='1', size='l')
for x, role, items in [(22, 'sujet', ['7 = 7 × 1', '−3 = −3 × 1']), (66, 'autre', ['a = a × 1', '2x + 3 = (2x + 3) × 1'])]:
    for k, t in enumerate(items):
        y = 28 - k * 15
        w = 38
        box(ax, x - w / 2, y - 5, w, 10, role, label=t, size='s')
        if k == 0: arrow(ax, (x, 43.5), (x, y + 5.3), 'varie', lw=1.0)
        else: text(ax, x, y + 9, '…', role, 'm')
text(ax, 44, 4, 'engendré par 1', 'varie', 's')
save(fig, '57-161')
