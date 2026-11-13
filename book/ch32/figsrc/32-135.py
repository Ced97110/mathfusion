import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(86)
a, b = 20.0, 34.64
ox, oy = 24, 20
box(ax, ox, oy, a, a, 'sujet', True, label=r'$\sin^2$', size='s', r=0.1)
box(ax, ox + a, oy, b, a, 'resultat', True, label=r'$\sin\cdot\cos$', size='s', r=0.1)
box(ax, ox, oy + a, a, b, 'resultat', True, label=r'$\sin\cdot\cos$', size='s', r=0.1)
box(ax, ox + a, oy + a, b, b, 'autre', True, label=r'$\cos^2$', size='m', r=0.1)
text(ax, ox + a / 2, oy + a + b + 4, r'$\sin\theta$', 'sujet', 's')
text(ax, ox + a + b / 2, oy + a + b + 4, r'$\cos\theta$', 'autre', 's')
text(ax, ox - 2, oy + a / 2, r'$\sin\theta$', 'sujet', 's', ha='right')
text(ax, ox - 2, oy + a + b / 2, r'$\cos\theta$', 'autre', 's', ha='right')
text(ax, 44, 12, r'$\sin^2+\cos^2=1$', 'encre', 's')
text(ax, 44, 5, r'$(\sin+\cos)^2=1+2\sin\cos$', 'encre', 's')
save(fig, '32-135')
