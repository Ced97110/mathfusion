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
box(ax, 32, 4, 22, 62, 'fixe', False, dash=True)
text(ax, 43, 59, "test dans\n$\\sin+\\cos=1$", 'encre', 's')
ys = [50, 38, 26, 14]
for y, a, r, ty in zip(ys, ['0°', '90°', '180°', '270°'], ['resultat'] * 2 + ['limite'] * 2, [48, 42, 24, 16]):
    box(ax, 2, y, 16, 9, 'fixe', True, label=a, size='m')
    arrow(ax, (18, y + 4.5), (64, ty), r)
box(ax, 64, 34, 22, 26, 'resultat', True, label='gardés\n0° et 90°', size='s')
box(ax, 64, 6, 22, 26, 'limite', True, label='rejetés\n180° et 270°', size='s')
save(fig, '32-136')
