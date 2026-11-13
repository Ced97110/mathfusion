import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(60)
yt, yb = 46, 16
ft = numberline(ax, 14, 62, yt, -1, 2, arrow_right=False)
fb = numberline(ax, 14, 62, yb, -1, 2, labels=False, arrow_right=False)
text(ax, 77, yt, r'$x^2=x$', 'sujet', 'm'); text(ax, 77, yb, r'$x=1$', 'sujet', 'm')
for v in (0, 1): dot(ax, ft(v), yt, 'resultat', 1.7)
dot(ax, fb(1), yb, 'resultat', 1.7)
ax.add_patch(Circle((fb(0), yb), 1.8, ec=COL['varie'], fc='none', ls='--', lw=1.0, zorder=4))
text(ax, fb(0), yb - 5, r'$x=0$ perdu', 'varie', 's')
arrow(ax, (fb(0.5), yt - 6), (fb(0.5), yb + 6), 'varie')
text(ax, 58, 31, r'on divise par $x$', 'varie', 's')
save(fig, '32-139')
