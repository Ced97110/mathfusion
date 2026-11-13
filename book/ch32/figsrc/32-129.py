import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(68)
cx, cy, R = 30, 30, 24
circ(ax, cx, cy, R)
line(ax, [(cx - 28, cy + R), (cx + 28, cy + R)], 'sujet', lw=1.1)
line(ax, [(cx, cy), (cx, cy + R)], 'sujet', lw=1.1, dash=True)
dot(ax, cx, cy + R, 'resultat', 1.7)
text(ax, cx, cy + R + 7, r'$P$ : 90°', 'resultat', 's')
text(ax, cx + 13, cy + 12, 'hauteur 1', 'sujet', 's')
text(ax, 72, cy + R, r'droite $y=1$', 'sujet', 's')
text(ax, 72, 38, r'$\sin x=1$', 'encre', 'l')
text(ax, 72, 30, r'$x=90°$', 'resultat', 'l')
save(fig, '32-129')
