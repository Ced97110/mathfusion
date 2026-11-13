import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(58)
yt, yb = 44, 14
ft = numberline(ax, 12, 64, yt, -2, 2, labels=False, arrow_right=False)
fb = numberline(ax, 12, 64, yb, -2, 2, every=2, arrow_right=False)
text(ax, 76, yt, r'$x=1$', 'sujet', 'm')
text(ax, 76, yb, r'$x^2=1$', 'varie', 'm')
dot(ax, ft(1), yt, 'resultat', 1.7); text(ax, ft(1), yt + 4.5, '1', 'resultat', 's')
dot(ax, fb(1), yb, 'resultat', 1.7); text(ax, fb(1), yb + 4.5, '1', 'resultat', 's')
dot(ax, fb(-1), yb, 'varie', 1.7); text(ax, fb(-1), yb + 4.5, r'$-1$ ajouté', 'varie', 's')
arrow(ax, (ft(0), yt - 5), (ft(0), yb + 9), 'varie')
text(ax, ft(0) + 6, 29, 'au carré', 'varie', 's', ha='left')
save(fig, '32-134')
