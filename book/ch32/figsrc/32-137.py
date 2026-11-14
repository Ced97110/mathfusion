import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(66)
box(ax, 2, 16, 84, 48, 'fixe', False, dash=True)
text(ax, 44, 59, 'produits par le calcul', 'fixe', 's')
box(ax, 6, 22, 36, 28, 'resultat', True)
text(ax, 24, 40, '0° et 90°', 'resultat', 'l')
text(ax, 24, 30, 'solutions', 'resultat', 's')
box(ax, 46, 22, 36, 28, 'limite', True)
text(ax, 64, 40, '180° et 270°', 'limite', 'l')
text(ax, 64, 30, 'parasites', 'limite', 's')
box(ax, 14, 2, 60, 9, 'fixe', True, label="45° : faux, hors du calcul", size='s')
save(fig, '32-137')
