import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cells(ax, x0, y, cw, h, n, k, on):
    for i in range(n):
        r = on if i < k else 'fixe'
        ax.add_patch(Rectangle((x0 + i * cw, y), cw, h, ec=COL['fixe'], fc=FILL[r], lw=0.5, zorder=2))
    ax.add_patch(Rectangle((x0, y), n * cw, h, ec=COL[on], fc='none', lw=0.9, zorder=3))
fig, ax = canvas(62)
x0, cw = 6.0, 5.0
text(ax, x0, 54, r'$P=\frac{2}{3}$', 'sujet', 'm', ha='left')
cells(ax, x0, 40, cw, 8, 15, 10, 'sujet')
text(ax, x0, 31, r'$Q=\frac{3}{5}$', 'autre', 'm', ha='left')
cells(ax, x0, 17, cw, 8, 15, 9, 'autre')
for k in (9, 10):
    line(ax, [(x0 + k * cw, 15), (x0 + k * cw, 50)], 'fixe', lw=0.9, dash=True)
text(ax, x0 + 9 * cw - 1.5, 52, '9', 'autre', 's'); text(ax, x0 + 10 * cw + 1.5, 52, '10', 'sujet', 's')
ax.add_patch(Rectangle((x0 + 9 * cw, 17), cw, 8, ec=COL['varie'], fc='none', lw=1.2, zorder=4))
brace(ax, x0 + 9 * cw, x0 + 10 * cw, 15, 'varie', '1 quinzième', down=True)
text(ax, 80, 52, '15 parts', 'fixe', 's', ha='right')
save(fig, '07-056')
