import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(72)
box(ax, 24, 58, 40, 11, 'varie', True, label=r'$(x+y)^2=1$', size='m')
box(ax, 4, 36, 34, 11, 'sujet', True, label=r'$x+y=1$', size='m')
box(ax, 50, 36, 34, 11, 'limite', True, label=r'$x+y=-1$', size='m')
arrow(ax, (34, 58), (21, 47), 'varie'); arrow(ax, (54, 58), (67, 47), 'varie')
text(ax, 21, 31, r'$1^2=1$', 'sujet', 's'); text(ax, 67, 31, r'$(-1)^2=1$', 'limite', 's')
arrow(ax, (21, 27), (21, 21), 'sujet'); arrow(ax, (67, 27), (67, 21), 'limite')
box(ax, 4, 9, 34, 12, 'resultat', True, label='points $A$, $B$', size='s')
box(ax, 50, 9, 34, 12, 'limite', True, label='points $C$, $D$', size='s')
text(ax, 21, 4, 'équation de départ', 'sujet', 's'); text(ax, 67, 4, 'ajoutée par le carré', 'limite', 's')
save(fig, '32-138')
