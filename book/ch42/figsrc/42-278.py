import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

from matplotlib.patches import Circle
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import numpy as np
fig, ax = canvas(72)
def venn_frame(x0, y0, w, h):
    box(ax, x0, y0, w, h, 'fixe', fill=False)
    text(ax, x0 + 4, y0 + h - 3.5, r'$U$', 'fixe', 's')
def circles(x0, y0, w, h, fillc):
    cy = y0 + h / 2 - 1; cx = x0 + w / 2
    for dx, role in ((-6, 'sujet'), (6, 'autre')):
        ax.add_patch(Circle((cx + dx, cy), 9, fc=fillc, ec=COL[role], lw=0.9, zorder=3))
    text(ax, cx - 10.5, cy, r'$A$', 'sujet', 'm'); text(ax, cx + 10.5, cy, r'$B$', 'autre', 'm')
    return cx, cy
def outside(x0, y0, w, h, cx, cy, role):
    t = np.linspace(0, 2 * np.pi, 80)
    ring = np.c_[cx + 9 * np.cos(-t), cy + 9 * np.sin(-t)]
    rect = np.array([(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)])
    verts = np.vstack([rect, rect[:1], ring, ring[:1]])
    codes = [Path.MOVETO] + [Path.LINETO] * 3 + [Path.CLOSEPOLY] + [Path.MOVETO] + [Path.LINETO] * (len(ring) - 1) + [Path.CLOSEPOLY]
    ax.add_patch(PathPatch(Path(verts, codes), fc=COL[role], alpha=0.22, ec='none', zorder=2))
x0, y0, w, h = 3, 14, 38, 34
box(ax, x0, y0, w, h, 'resultat')
cx, cy = circles(x0, y0, w, h, 'white'); venn_frame(x0, y0, w, h)
X0 = 47
venn_frame(X0, y0, w, h)
box(ax, X0, y0, w, h, 'fixe', fill=False)
cx2, cy2 = circles(X0, y0, w, h, 'none')
outside(X0, y0, w, h, cx2 - 6, cy2, 'sujet'); outside(X0, y0, w, h, cx2 + 6, cy2, 'autre')
text(ax, 22, 56, r"$(A\cup B)'$", 'resultat', 'l'); text(ax, 66, 56, r"$A'\cap B'$", 'resultat', 'l')
text(ax, 22, y0 + 4, r'hors de $A\cup B$', 'resultat', 's'); text(ax, 66, y0 + 4, r'hors de $A$ et de $B$', 'fixe', 's')
text(ax, 44, 31, r'$=$', 'encre', 'l')
text(ax, 44, 6, r'pour tous $A$ et $B$ de $U$', 'sujet', 's')
save(fig, '42-278')
