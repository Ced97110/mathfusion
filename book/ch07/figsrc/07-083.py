import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(60)
x0, pw = 8, 12.6
for i in range(5):
    role = 'sujet' if i < 3 else 'varie'
    seg(ax, x0 + i * pw, 28, pw, 10, role)
    text(ax, x0 + i * pw + pw / 2, 33, '1/4', role, 's')
seg(ax, x0, 26.5, 4 * pw, 13, 'fixe', dash=True, filled=False)
text(ax, x0 + 2 * pw, 45, '1 entier = 4 parts', 'fixe', 's')
c4 = x0 + 4.5 * pw
arrow(ax, (c4, 46), (c4, 40.5), 'varie')
text(ax, c4, 49.5, 'dépasse 1 entier', 'varie', 's')
brace(ax, x0 + 0.3, x0 + 3 * pw - 0.3, 26, 'sujet', '3 parts')
brace(ax, x0 + 3 * pw + 0.3, x0 + 5 * pw, 26, 'varie', '+ 2 parts')
text(ax, 44, 8, '5 parts de 1/4 : 5/4', 'resultat', 'm', weight='bold')
save(fig, '07-083')
