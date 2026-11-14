import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(70)
box(ax, 3, 54, 26, 11, 'sujet', True, label=r'$x=1$', size='m')
arrow(ax, (29, 59.5), (57, 59.5), 'varie'); text(ax, 43, 64, 'au carré', 'varie', 's')
box(ax, 57, 54, 26, 11, 'varie', True, label=r'$x^2=1$', size='m')
arrow(ax, (70, 54), (57, 45), 'varie'); arrow(ax, (70, 54), (75, 45), 'varie')
box(ax, 50, 33, 14, 12, 'fixe', True, label='1', size='m')
box(ax, 68, 33, 14, 12, 'fixe', True, label=r'$-1$', size='m')
arrow(ax, (57, 33), (57, 22), 'resultat'); arrow(ax, (75, 33), (75, 22), 'limite')
box(ax, 50, 8, 14, 14, 'resultat', True, label='vrai', size='s')
box(ax, 68, 8, 14, 14, 'limite', True, label='faux', size='s')
text(ax, 22, 28, r'vérifier dans $x=1$', 'sujet', 's')
save(fig, '32-140')
