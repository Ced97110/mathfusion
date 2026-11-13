import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cells(ax, x0, y, cw, h, n, k, on, off='fixe'):
    for i in range(n):
        r = on if i < k else off
        ax.add_patch(Rectangle((x0 + i * cw, y), cw, h, ec=COL[r], fc=FILL[r], lw=0.6, zorder=2))
fig, ax = canvas(62)
u, x0, y, h = 8.4, 6.0, 30.0, 8.0
text(ax, 44, 57, r'$8\ \frac{3}{5}\ =\ 8+\frac{3}{5}$', 'encre', 'l')
for i in range(8):
    ax.add_patch(Rectangle((x0 + i * u, y), u, h, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=2))
    for j in range(1, 5):
        xx = x0 + i * u + j * u / 5
        ax.plot([xx, xx], [y, y + h], color=COL['fixe'], lw=0.4, zorder=3)
xp = x0 + 8 * u
ax.add_patch(Rectangle((xp, y), u, h, ec=COL['fixe'], fc='none', lw=0.8, ls='--', zorder=2))
ax.add_patch(Rectangle((xp, y), 3 * u / 5, h, ec=COL['varie'], fc=FILL['varie'], lw=0.9, zorder=2))
for j in range(1, 5):
    xx = xp + j * u / 5
    ax.plot([xx, xx], [y, y + h], color=COL['fixe'], lw=0.4, zorder=3)
brace(ax, x0, x0 + 8 * u, y + h + 1.5, 'sujet', '8 unités', down=False)
brace(ax, xp, xp + 3 * u / 5, y + h + 1.5, 'varie', r'$\frac{3}{5}$', down=False)
brace(ax, x0, x0 + 8 * u, y - 1.5, 'sujet', '5 cinquièmes par unité')
text(ax, 44, 12, r'$\frac{40}{5}+\frac{3}{5}=\frac{43}{5}$', 'resultat', 'l')
save(fig, '07-049')
