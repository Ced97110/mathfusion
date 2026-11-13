import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for y, p in [(38, 35), (24, 7), (10, 80)]:
    for i in range(100):
        r = 'sujet' if i < p else 'fixe'
        ax.add_patch(Rectangle((20 + i * 0.48, y), 0.48, 6, ec=COL[r], fc=FILL[r], lw=0.15, zorder=2))
    text(ax, 11, y + 3, f'{p} %', 'sujet', 'm')
    text(ax, 78, y + 3, f'p = {p}', 'sujet', 'm')
brace(ax, 20, 68, 9, 'fixe', label='toujours 100 parts')
brace(ax, 20, 68, 45.5, 'fixe', down=False, label=None) if False else None
save(fig, '09-068')
