import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cells(ax, x0, y, cw, h, n, k, on):
    for i in range(n):
        r = on if i < k else 'fixe'
        ax.add_patch(Rectangle((x0 + i * cw, y), cw, h, ec=COL['fixe'], fc=FILL[r], lw=0.5, zorder=2))
    ax.add_patch(Rectangle((x0, y), n * cw, h, ec=COL[on], fc='none', lw=0.9, zorder=3))
fig, ax = canvas(66)
x0, cw = 17.0, 4.4
cells(ax, x0, 44, cw, 8, 15, 10, 'sujet'); text(ax, 9, 48, r'$\frac{2}{3}$', 'sujet', 'l')
cells(ax, x0, 26, cw, 8, 15, 9, 'autre'); text(ax, 9, 30, r'$\frac{3}{5}$', 'autre', 'l')
brace(ax, x0, x0 + 10 * cw, 53.5, 'sujet', '10 quinzièmes', down=False)
brace(ax, x0, x0 + 9 * cw, 24.5, 'autre', '9 quinzièmes', down=True)
text(ax, 44, 7, r'$\frac{10}{15}>\frac{9}{15}$', 'resultat', 'l')
save(fig, '07-057')
