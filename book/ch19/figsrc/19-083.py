import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
cols = [10, 28, 47, 68]
rows = [(r'$-\frac{2}{3}$', '4'), (r'$-2$', '3'), (r'$m$', r'$b$')]
ys = [56, 34, 12]
# one dashed band per column: same place, same role in every row
ax.add_patch(Rectangle((cols[1] - 11, 2), 22, 62, fc='none', ec=COL['sujet'], lw=0.9, ls='--', zorder=1))
ax.add_patch(Rectangle((cols[3] - 10, 2), 20, 62, fc='none', ec=COL['autre'], lw=0.9, ls='--', zorder=1))
for k, (m, b) in enumerate(rows):
    y = ys[k]
    text(ax, cols[0], y, r'$y=$', 'encre', 'l')
    box(ax, cols[1] - 9, y - 7, 18, 14, 'sujet', label=m, size='l', weight='bold' if k == 2 else 'normal')
    text(ax, cols[2], y, r'$x\ +$', 'encre', 'l')
    box(ax, cols[3] - 8, y - 7, 16, 14, 'autre', label=b, size='l', weight='bold' if k == 2 else 'normal')
line(ax, [(2, 45), (86, 45)], 'fixe', dash=True); line(ax, [(2, 23), (86, 23)], 'fixe', dash=True)
text(ax, cols[1], 70, r'devant $x$ : $m$', 'sujet', 's'); text(ax, cols[3], 70, r'nombre seul : $b$', 'autre', 's')
save(fig, '19-083')
