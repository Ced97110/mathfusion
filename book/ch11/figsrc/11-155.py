import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Ellipse
fig, ax = canvas(74)
def cyl(cx, yb, w, h, role):
    e = 0.22 * w
    ax.add_patch(Ellipse((cx, yb), w, 2 * e, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    ax.add_patch(Rectangle((cx - w / 2, yb), w, h, ec='none', fc=FILL[role], zorder=2.1))
    line(ax, [(cx - w / 2, yb), (cx - w / 2, yb + h)], role); line(ax, [(cx + w / 2, yb), (cx + w / 2, yb + h)], role)
    ax.add_patch(Ellipse((cx, yb + h), w, 2 * e, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2.2))
cases = [(16, 'sujet', 10, 14, 'r = 3, h = 10', '≈ 282,6', ''),
         (45, 'varie', 20, 14, 'r = 6, h = 10', '≈ 1 130,4', 'V × 4'),
         (72, 'varie', 20, 28, 'r = 6, h = 20', '≈ 2 260,8', 'V × 8')]
for cx, role, w, h, lab, v, f in cases:
    cyl(cx, 22, w, h, role)
    text(ax, cx, 68, lab, role, 's')
    text(ax, cx, 12, v, role, 's')
    if f: text(ax, cx, 5, f, 'resultat', 'm', weight='bold')
text(ax, 16, 5, 'départ', 'sujet', 's')
text(ax, 44, 62, r'$V=\pi\times r^2\times h$', 'encre', 'm')
save(fig, '11-155')
