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
R = 15; cy = 32
cxl, cxr = 22, 66
circ(ax, cxl, cy, R); circ(ax, cxr, cy, R)
yk = cy + R / 2; d = math.sqrt(R * R - (R / 2) ** 2)
line(ax, [(cxl - 19, yk), (cxl + 19, yk)], 'sujet', lw=1.1)
dot(ax, cxl - d, yk, 'resultat', 1.6); dot(ax, cxl + d, yk, 'resultat', 1.6)
text(ax, cxl - d, yk + 5, r"$P'$", 'resultat', 's'); text(ax, cxl + d, yk + 5, r'$P$', 'resultat', 's')
line(ax, [(cxr - 19, cy + R), (cxr + 19, cy + R)], 'sujet', lw=1.1)
dot(ax, cxr, cy + R, 'resultat', 1.9)
text(ax, cxr, cy + R + 6, r"$P=P'$ : 90°", 'resultat', 's')
text(ax, cxl, 12, r'$-1<k<1$', 'sujet', 'm'); text(ax, cxl, 5, 'deux points', 'resultat', 's')
text(ax, cxr, 12, r'$k=1$', 'sujet', 'm'); text(ax, cxr, 5, 'un seul point', 'resultat', 's')
save(fig, '32-144')
