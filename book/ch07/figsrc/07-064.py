import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cells(ax, x0, y, cw, h, n, k, on, off='fixe'):
    for i in range(n):
        r = on if i < k else off
        ax.add_patch(Rectangle((x0 + i * cw, y), cw, h, ec=COL[r], fc=FILL[r], lw=0.6, zorder=2))
    ax.add_patch(Rectangle((x0, y), n * cw, h, ec=COL[on], fc='none', lw=0.9, zorder=3))
fig, ax = canvas(76)
x0, cw = 12.0, 16.0
text(ax, 44, 70, r'$\frac{1}{2}$ litre de jus', 'sujet', 'm')
cells(ax, x0, 54, cw, 7, 4, 2, 'sujet')
text(ax, 44, 44, r'verre : $\frac{3}{4}$ de litre', 'autre', 'm')
cells(ax, x0, 28, cw, 7, 3, 3, 'autre', 'autre')
for i in range(2): ax.add_patch(Rectangle((x0 + i * cw, 28), cw, 7, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=3))
brace(ax, x0, x0 + 2 * cw, 26.5, 'resultat', '2 parts sur 3', down=True)
text(ax, 44, 8, r'$\dfrac{\frac{1}{2}}{\frac{3}{4}}=\frac{2}{3}$ de verre', 'resultat', 'm')
save(fig, '07-064')
