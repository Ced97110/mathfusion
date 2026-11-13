import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cells(ax, x0, y, cw, h, n, k, on, off='fixe'):
    for i in range(n):
        r = on if i < k else off
        ax.add_patch(Rectangle((x0 + i * cw, y), cw, h, ec=COL[r], fc=FILL[r], lw=0.6, zorder=2))
    ax.add_patch(Rectangle((x0, y), n * cw, h, ec=COL[on], fc='none', lw=0.9, zorder=3))
fig, ax = canvas(62)
cw, x0 = 9.0, 8.0
text(ax, x0, 54, r'$\frac{3}{8}$', 'sujet', 'l', ha='left')
cells(ax, x0, 40, cw, 8, 8, 3, 'sujet')
text(ax, x0, 33, r'$\frac{5}{8}$', 'autre', 'l', ha='left')
cells(ax, x0, 19, cw, 8, 8, 5, 'autre')
text(ax, 44, 36, '3 parts', 'sujet', 's'); text(ax, 44, 15, '5 parts', 'autre', 's')
text(ax, 44, 8, r'$\frac{3}{8}<\frac{5}{8}$', 'resultat', 'l')
text(ax, 70, 54, '8 parts égales', 'fixe', 's')
save(fig, '07-050')
