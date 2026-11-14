import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 4, 74, 'ℤ : on alterne', 'sujet', 'm', ha='left')
vals = ['0', '1', r'$-1$', '2', r'$-2$']
for i, v in enumerate(vals):
    x = 11 + 15 * i
    box(ax, x - 6, 54, 12, 9, 'sujet', label=v)
    text(ax, x, 48, str(i), 'varie', 's')
text(ax, 85, 58.5, '…', 'sujet', 'l')
text(ax, 4, 38, 'ℚ : couples en diagonales', 'autre', 'm', ha='left')
pts = {(m, n): (14 + 14 * m, 8 + 9 * n) for m in range(3) for n in range(3)}
order = [(0, 0), (1, 0), (0, 1), (0, 2), (1, 1), (2, 0)]
line(ax, [pts[p] for p in order], 'autre', lw=1.0)
for p, (x, y) in pts.items():
    disc(ax, x, y, 1.8, 'autre')
arrow(ax, pts[(2, 0)], (pts[(2, 0)][0] + 12, pts[(2, 0)][1] + 4), 'autre')
text(ax, 70, 16, '…', 'autre', 'l')
save(fig, '43-116')
