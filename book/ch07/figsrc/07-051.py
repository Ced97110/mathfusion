import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cells(ax, x0, y, cw, h, n, k, on, off='fixe'):
    for i in range(n):
        r = on if i < k else off
        ax.add_patch(Rectangle((x0 + i * cw, y), cw, h, ec=COL[r], fc=FILL[r], lw=0.6, zorder=2))
    ax.add_patch(Rectangle((x0, y), n * cw, h, ec=COL[on], fc='none', lw=0.9, zorder=3))
fig, ax = canvas(80)
x0, L = 16.0, 68.0
rows = [(68, 3, 2, 'sujet', r'$\frac{2}{3}$'), (56, 5, 3, 'autre', r'$\frac{3}{5}$'),
        (34, 15, 10, 'sujet', r'$\frac{10}{15}$'), (22, 15, 9, 'autre', r'$\frac{9}{15}$')]
for y, n, k, role, lab in rows:
    cells(ax, x0, y, L / n, 7, n, k, role)
    text(ax, 8, y + 3.5, lab, role, 'm')
arrow(ax, (50, 54), (50, 44), 'varie')
text(ax, 54, 49, 'recouper en 15', 'varie', 's', ha='left')
text(ax, 44, 8, r'$10>9$, donc $\frac{2}{3}>\frac{3}{5}$', 'resultat', 'l')
save(fig, '07-051')
