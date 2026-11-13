import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax, x, y, w, h, role, dash=False, filled=True):
    ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role] if filled else "none", lw=0.8, ls="--" if dash else "-", zorder=2))
fig, ax = canvas(64)
f = numberline(ax, 10, 70, 30, -3, 3)
disc(ax, f(1), 30, 1.4, 'sujet'); disc(ax, f(-2), 30, 1.4, 'resultat')
arrow(ax, (f(1) - 1, 32), (f(-2) + 1, 32), 'varie', curve=0.45)
text(ax, (f(1) + f(-2)) / 2, 43, 'retire 3', 'varie', 's')
text(ax, f(1), 20, 'départ', 'sujet', 's'); text(ax, f(-2), 20, 'arrivée', 'resultat', 's')
text(ax, 44, 57, '(1 − 3)/4 = −2/4 = −1/2', 'encre', 'l')
text(ax, 44, 8, 'seul le haut devient négatif', 'fixe', 's')
save(fig, '07-090')
