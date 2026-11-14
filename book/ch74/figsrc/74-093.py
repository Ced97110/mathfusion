import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 8
def panel(cx, cy, k, role):
    ax.add_patch(Circle((cx, cy), u, fill=False, ec=COL['fixe'], lw=0.7, ls='--', zorder=1))
    arrow(ax, (cx, cy), (cx, cy + k*u), role, lw=1.4)
    arrow(ax, (cx, cy), (cx - k*u, cy), role, lw=1.4)
    disc(ax, cx, cy, 0.8, 'encre')
panel(22, 28, 1, 'resultat')
panel(66, 28, 2, 'limite')
text(ax, 22, 52, 'quart de tour', 'resultat', 's')
text(ax, 22, 48.5, 'colonnes de longueur 1', 'resultat', 's')
text(ax, 66, 52, 'double les longueurs', 'limite', 's')
text(ax, 66, 48.5, 'colonnes de longueur 2', 'limite', 's')
text(ax, 22, 10, r'dans $O(2)$', 'resultat', 'm')
text(ax, 66, 10, r'pas dans $O(2)$', 'limite', 'm')
text(ax, 44, 59, 'cercle gris : longueur 1', 'fixe', 's')
save(fig, '74-093')
