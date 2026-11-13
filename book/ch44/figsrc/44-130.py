import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 2, 12, 34, 34, 'fixe'); box(ax, 52, 12, 34, 34, 'sujet')
text(ax, 19, 50, 'ℚ', 'fixe', 'l'); text(ax, 69, 50, r'ℚ$^*$', 'sujet', 'l')
vals = [r'$-\frac{1}{2}$', '0', r'$\frac{3}{4}$', '2']
for k, v in enumerate(vals):
    y = 40 - k * 8
    disc(ax, 19, y, 3.4, 'limite' if v == '0' else 'fixe', label=v, size='s')
    if v == '0':
        disc(ax, 69, y, 3.4, 'limite', fill=False, label='0', size='s'); ax.plot([66.5, 71.5], [y - 2.5, y + 2.5], color=COL['limite'], lw=0.9, zorder=6)
    else:
        disc(ax, 69, y, 3.4, 'sujet', label=v, size='s')
arrow(ax, (38, 29), (50, 29), 'varie', lw=1.4)
text(ax, 44, 33, r'$*$', 'varie', 'xl'); text(ax, 44, 24, 'sans 0', 'varie', 's')
save(fig, '44-130')
