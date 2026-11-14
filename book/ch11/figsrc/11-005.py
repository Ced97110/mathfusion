import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
c = 3.2; gx, gy = 2, 4
for i in range(12):
    for j in range(8):
        ax.add_patch(Rectangle((gx + i * c, gy + j * c), c, c, ec=COL['sujet'], fc=FILL['sujet'], lw=0.4, zorder=2))
for i in range(12):
    line(ax, [(gx + i * c + 0.4, gy + 8 * c + 3), (gx + (i + 1) * c - 0.4, gy + 8 * c + 3)], 'varie', lw=1.8)
text(ax, gx + 6 * c, gy + 8 * c + 7, 'étalon : 1 m', 'varie', 's')
box(ax, 50, 36, 36, 9, 'varie', label='longueur : 12 segments', size='s')
arrow(ax, (50, 40.5), (gx + 12 * c + 1, 33.4), 'varie')
box(ax, 50, 14, 36, 9, 'sujet', label='surface : 96 carrés', size='s')
arrow(ax, (50, 18.5), (gx + 12 * c + 1, 16), 'sujet')
save(fig, '11-005')
