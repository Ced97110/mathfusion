import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(64)
t, x0 = 6.4, 8
seg(ax, x0, 50, 2 * t, 9, 'sujet'); seg(ax, x0 + 2 * t, 50, 2 * t, 9, 'fixe', dash=True, filled=False)
text(ax, x0 + t, 54.5, '1/2', 'sujet', 's')
text(ax, 40, 54.5, '+', 'fixe', 'l'); box(ax, 48, 50, 24, 9, 'autre', label='9/4')
arrow(ax, (x0 + t, 49.5), (x0 + t, 36), 'varie')
text(ax, x0 + t + 4, 43, 'recoupé en quarts', 'varie', 's', ha='left')
for i in range(11):
    seg(ax, x0 + i * t, 26, t, 9, 'sujet' if i < 2 else 'autre')
brace(ax, x0 + 0.3, x0 + 2 * t - 0.3, 25, 'sujet', '2/4')
brace(ax, x0 + 2 * t + 0.3, x0 + 11 * t, 25, 'autre', '9/4')
brace(ax, x0 + 0.3, x0 + 11 * t, 13, 'resultat', '11/4')
save(fig, '07-089')
