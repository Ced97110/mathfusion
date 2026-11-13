import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(70)
text(ax, 22, 63, 'recette A', 'sujet', 'm'); text(ax, 66, 63, 'recette B', 'autre', 'm')
text(ax, 22, 40, r'$\frac{2}{3}$', 'sujet', 'xl'); text(ax, 66, 40, r'$\frac{3}{5}$', 'autre', 'xl')
arrow(ax, (27, 43.5), (60, 36.5), 'varie'); arrow(ax, (27, 36.5), (60, 43.5), 'varie')
text(ax, 22, 52, r'$2\times 5=10$', 'varie', 'm'); text(ax, 22, 28, r'$3\times 3=9$', 'varie', 'm')
text(ax, 44, 14, '10 > 9 : A a plus de sirop', 'resultat', 'm', weight='bold')
save(fig, '07-087')
