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
box(ax, 14, 52, 60, 11, 'sujet', True, label=r'vérifier $k$ avant tout', size='m')
arrow(ax, (44, 52), (44, 44), 'sujet')
box(ax, 24, 33, 40, 11, 'varie', True, label=r'$-1\leq k\leq 1$ ?', size='m')
arrow(ax, (34, 33), (22, 21), 'resultat'); arrow(ax, (54, 33), (66, 21), 'fixe')
text(ax, 22, 29, 'oui', 'resultat', 's'); text(ax, 67, 29, 'non', 'fixe', 's')
box(ax, 2, 6, 40, 15, 'resultat', True, label='calculatrice :\n$\\sin^{-1}$ de $k$', size='s')
box(ax, 46, 6, 40, 15, 'fixe', True, label="aucune solution,\non s'arrête", size='s')
save(fig, '32-143')
