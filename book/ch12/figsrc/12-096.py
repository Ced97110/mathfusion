import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, r=1.1, hollow=False):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc="white" if hollow else COL[role], lw=0.9, zorder=6))

fig, ax = canvas(68)
y = 34
f = numberline(ax, 8, 68, y, 0, 7, labels=False, arrow_right=False)
text(ax, f(0), y - 4.5, '0', 'fixe', 'm')
dot(ax, f(7), y, 'resultat', 1.6); text(ax, f(7), y - 4.5, '7', 'resultat', 'm')
# path 1 above: 3 then 4
arrow(ax, (f(0), y + 2), (f(3), y + 2), 'sujet', curve=-0.45)
arrow(ax, (f(3), y + 2), (f(7) - 1, y + 2), 'autre', curve=-0.45)
text(ax, f(1.5), y + 10, '3', 'sujet', 'm'); text(ax, f(5), y + 12, '4', 'autre', 'm')
text(ax, 44, 56, '3 + 4', 'encre', 'l')
# path 2 below: 4 then 3
arrow(ax, (f(0), y - 8), (f(4), y - 8), 'autre', curve=0.45)
arrow(ax, (f(4), y - 8), (f(7) - 1, y - 8), 'sujet', curve=0.45)
text(ax, f(2), y - 20, '4', 'autre', 'm'); text(ax, f(5.5), y - 18, '3', 'sujet', 'm')
text(ax, 44, 4, '4 + 3 : même arrivée', 'resultat', 'm')
save(fig, '12-096')
