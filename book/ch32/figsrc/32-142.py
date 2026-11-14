import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circ(ax, cx, cy, R, ext=4):
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.5)
    ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.9, zorder=2))

def dot(ax, x, y, role, r=1.4):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))

def onc(cx, cy, R, deg):
    return (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
fig, ax = canvas(64)
box(ax, 3, 48, 32, 12, 'sujet', True, label=r'$\sin x-2=0$', size='m')
arrow(ax, (35, 54), (53, 54), 'varie'); text(ax, 44, 59, 'ajouter 2', 'varie', 's')
box(ax, 55, 48, 30, 12, 'varie', True, label=r'$\sin x=2$', size='m')
y = 22
f = numberline(ax, 10, 66, y, -2, 3)
ax.add_patch(Rectangle((f(-1), y - 1.3), f(1) - f(-1), 2.6, ec=COL['resultat'], fc=FILL['resultat'], lw=0.9, zorder=2.5))
text(ax, f(0), y + 8, 'valeurs du sinus', 'resultat', 's')
dot(ax, f(2), y, 'limite', 1.7); text(ax, f(2) + 3, y + 8, 'impossible', 'limite', 's')
save(fig, '32-142')
