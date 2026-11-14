import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cxm = 47
y0, y1, y2, h = 6, 22, 38, 10
box(ax, cxm - 7, y0, 14, h, 'fixe', label='a')
box(ax, cxm - 14, y1, 14, h, 'sujet', label='a')
box(ax, cxm, y1, 14, h, 'sujet', label='b√5')
box(ax, cxm - 28, y2, 28, h, 'sujet', label='a + b√5')
box(ax, cxm, y2, 28, h, 'autre', label='(c + d√5)ζ')
for y, nm, d in [(y0, 'ℚ', 'dim 1'), (y1, 'ℚ(√5)', 'dim 2'), (y2, 'ℚ(ζ₅)', 'dim 4')]:
    text(ax, 2, y + h / 2, nm, 'encre', 'm', ha='left')
    text(ax, 80, y + h / 2, d, 'varie', 's', ha='left')
for y in (y0, y1):
    arrow(ax, (cxm, y + h + 0.4), (cxm, y + 16 - 0.4), 'varie')
    text(ax, cxm + 5, y + h + 3, '×2', 'varie', 's')
save(fig, '66-096')
