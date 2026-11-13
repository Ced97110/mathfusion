import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cells(ax, x0, y, cw, h, n, k, on, off='fixe'):
    for i in range(n):
        r = on if i < k else off
        ax.add_patch(Rectangle((x0 + i * cw, y), cw, h, ec=COL[r], fc=FILL[r], lw=0.6, zorder=2))
    ax.add_patch(Rectangle((x0, y), n * cw, h, ec=COL[on], fc='none', lw=0.9, zorder=3))
fig, ax = canvas(70)
text(ax, 44, 64, 'se lit : « est plus grand que »', 'resultat', 'm')
for i in range(5): disc(ax, 8 + i * 5, 50, 1.9, 'sujet')
for i in range(2): disc(ax, 62 + i * 5, 50, 1.9, 'autre')
text(ax, 18, 40, '5', 'sujet', 'xl'); text(ax, 67, 40, '2', 'autre', 'xl')
text(ax, 44, 48, '>', 'resultat', 22, weight='bold')
cells(ax, 6, 14, 6, 6, 4, 3, 'sujet'); cells(ax, 58, 14, 6, 6, 2, 1, 'autre')
text(ax, 18, 26, r'$\frac{3}{4}$', 'sujet', 'l'); text(ax, 70, 26, r'$\frac{1}{2}$', 'autre', 'l')
text(ax, 44, 17, '>', 'resultat', 22, weight='bold')
save(fig, '07-052')
