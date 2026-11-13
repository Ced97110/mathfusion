import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(74)
cx, cy, R = 44, 40, 12
circ(ax, cx, cy, R)
line(ax, [(4, cy + 2 * R), (84, cy + 2 * R)], 'sujet', lw=1.1)
line(ax, [(4, cy - 3 * R), (84, cy - 3 * R)], 'sujet', lw=1.1)
text(ax, 66, cy + 2 * R + 4, r'$y=2$ ($k>1$)', 'sujet', 's')
text(ax, 66, cy - 3 * R + 4, r'$y=-3$ ($k<-1$)', 'sujet', 's')
text(ax, cx + 3, cy + R + 2.5, '1', 'fixe', 's'); text(ax, cx + 4.5, cy - R - 2.5, r'$-1$', 'fixe', 's')
text(ax, 74, 40, 'aucun point\ncommun', 'encre', 's')
save(fig, '32-141')
