import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ax0, y0, s = 30, 8, 0.5
arrow(ax, (ax0, y0), (ax0, y0 + 100 * s + 8), 'autre')
text(ax, ax0, y0 + 100 * s + 12, 'm', 'autre', 'xl', weight='bold')
for m in (0, 25, 50, 100):
    ax.plot([ax0 - 1.2, ax0 + 1.2], [y0 + m * s] * 2, color=COL['autre'], lw=0.8)
    text(ax, ax0 - 5, y0 + m * s, str(m), 'autre', 's')
for m in (25, 50, 100):
    line(ax, [(ax0, y0 + m * s), (50, y0 + m * s)], 'varie', dash=True); disc(ax, 50, y0 + m * s, 1.8, 'varie')
text(ax, 62, 30, 'on lit en montant', 'autre', 's', ha='left')
arrow(ax, (60, 26), (60, 38), 'autre')
save(fig, '09-118')
