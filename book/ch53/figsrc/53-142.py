import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(102)
s = 6.2
text(ax, 44, 98, 'case = (reste par p, par q)', 'fixe', 's')
def grid(x0, ytop, nc, nr, mark, role):
    for r in range(nr):
        for c in range(nc):
            k = role if (r, c) == mark else 'fixe'
            ax.add_patch(Rectangle((x0 + c * s, ytop - (r + 1) * s), s, s, ec=COL[k], fc=FILL[k], lw=0.6, zorder=2))
# 5 et 11 : une case par nombre
text(ax, 44, 92, '5 et 11 : premiers entre eux', 'resultat', 's')
grid(2, 86, 11, 5, (0, 10), 'resultat')
text(ax, 86, 83, 'même case', 'resultat', 's', ha='right')
arrow(ax, (74, 83), (70.8, 83), 'resultat')
text(ax, 36, 51, '10 et 10⁸¹ : même case', 'resultat', 's')
# 4 et 6 : deux nombres dans la même case
text(ax, 44, 44, '4 et 6 : diviseur commun 2', 'limite', 's')
grid(2, 38, 6, 4, (0, 0), 'limite')
text(ax, 45, 33, '0 et 12 : même case', 'limite', 's', ha='left')
text(ax, 45, 27, 'mais 0 ≠ 12 (mod 24)', 'limite', 's', ha='left')
save(fig, '53-142')
