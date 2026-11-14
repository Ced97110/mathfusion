import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
counts = [1, 4, 12, 36, 108]; ratios = ['×4', '×3', '×3', '×3']
cur = 42.0; sp = 1.6; x0 = 19.0
for n, c in enumerate(counts):
    rows = (c + 35) // 36
    for k in range(c):
        r, i = divmod(k, 36)
        disc(ax, x0 + i * sp, cur - r * 2.0, 0.65, 'sujet')
    mid = cur - (rows - 1) * 1.0
    text(ax, 2, mid, f'niveau {n}', 'encre', 's', ha='left')
    text(ax, x0 + (min(c, 36) - 1) * sp + 3, mid, f'{c}'.replace('', '') if c < 100 else '108', 'sujet', 'm', ha='left', weight='bold')
    bottom = cur - (rows - 1) * 2.0
    if n < 4:
        gy = bottom - 3.5
        arrow(ax, (10, gy + 1.8), (10, gy - 1.8), 'varie')
        text(ax, 14, gy, ratios[n], 'varie', 's', ha='left')
    cur = bottom - 7.0
save(fig, '49-016')
