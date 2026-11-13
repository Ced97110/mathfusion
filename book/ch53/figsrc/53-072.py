import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle

assert 26 * 26 == 676
ES = (ord('E') - 65, ord('S') - 65)
QZ = (ord('Q') - 65, ord('Z') - 65)
assert ES == (4, 18) and QZ == (16, 25)

fig, ax = canvas(80)
c, x0, ytop = 2.0, 12, 66
ax.add_patch(Rectangle((x0, ytop - 26 * c), 26 * c, 26 * c, fc=FILL['fixe'], ec=COL['fixe'], lw=0.6, zorder=2))
for k in range(27):
    ax.plot([x0 + k * c] * 2, [ytop - 26 * c, ytop], color=COL['fixe'], lw=0.15, zorder=3)
    ax.plot([x0, x0 + 26 * c], [ytop - k * c] * 2, color=COL['fixe'], lw=0.15, zorder=3)
def cell(rc, role):
    i, j = rc
    cx, cy = x0 + (j + 0.5) * c, ytop - (i + 0.5) * c
    ax.add_patch(Rectangle((cx - 1.8, cy - 1.8), 3.6, 3.6, fc=FILL[role], ec=COL[role], lw=1.0, zorder=4))
    return cx, cy
ex, ey = cell(ES, 'resultat')
qx, qy = cell(QZ, 'limite')
text(ax, 71, ey, 'ES :\nfréquente', 'resultat', 's', ha='left')
arrow(ax, (70, ey), (ex + 2.5, ey), 'resultat', lw=0.8)
text(ax, 71, qy, 'QZ :\nn’existe pas', 'limite', 's', ha='left')
arrow(ax, (70, qy), (qx + 2.5, qy), 'limite', lw=0.8)
text(ax, x0 + 13 * c, 71, r'2$^{e}$ lettre', 'fixe', 's')
text(ax, 7, ytop - 13 * c, r'1$^{re}$ lettre', 'fixe', 's', rot=90)
text(ax, x0 + 13 * c, 8, r'$26 \times 26 = 676$ paires', 'fixe', 's')
save(fig, '53-072')
