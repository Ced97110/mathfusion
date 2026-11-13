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
cx, cy, R = 30, 30, 24
circ(ax, cx, cy, R)
line(ax, [(cx, cy), (cx, cy + R)], 'sujet', lw=1.2)
dot(ax, cx, cy + R, 'sujet', 1.7)
text(ax, cx, cy + R + 8, r'$P$ : 90°', 'sujet', 's')
text(ax, cx - 2, cy + 12, 'montée 1', 'sujet', 's', ha='right')
text(ax, cx + 4, cy + R + 3, 'avancée 0', 'fixe', 's', ha='left')
text(ax, 72, 40, r'$\tan 90°=1\div0$', 'encre', 'm')
text(ax, 72, 30, "n'existe pas", 'varie', 'm')
save(fig, '32-130')
