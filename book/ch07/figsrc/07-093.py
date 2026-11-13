import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(66)
text(ax, 15, 59, 'départ', 'fixe', 's'); text(ax, 46, 59, 'multiplier par l’inverse', 'fixe', 's'); text(ax, 75, 59, 'résultat', 'fixe', 's')
text(ax, 14, 42, '(1/2)/(3/4)', 'sujet', 'l'); text(ax, 46, 42, r'$\frac{1}{2}\times\frac{4}{3}$', 'sujet', 'l'); text(ax, 75, 42, r'$\frac{2}{3}$', 'resultat', 'l')
text(ax, 14, 22, '(1/$x$)/(3/4)', 'varie', 'l'); text(ax, 46, 22, r'$\frac{1}{x}\times\frac{4}{3}$', 'varie', 'l'); text(ax, 75, 22, r'$\frac{4}{3x}$', 'resultat', 'l')
for y in (42, 22):
    arrow(ax, (27, y), (34, y), 'fixe'); arrow(ax, (59, y), (67, y), 'fixe')
text(ax, 44, 7, 'x est différent de 0', 'limite', 's')
save(fig, '07-093')
