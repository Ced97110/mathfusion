import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pp(c, R, d): return (c[0] + R * math.cos(math.radians(d)), c[1] + R * math.sin(math.radians(d)))
def axes_xy(ax, c, R, ext=4):
    arrow(ax, (c[0] - R - ext, c[1]), (c[0] + R + ext, c[1]), 'fixe', lw=0.7)
    arrow(ax, (c[0], c[1] - R - ext), (c[0], c[1] + R + ext), 'fixe', lw=0.7)
def ucirc(ax, c, R): ax.add_patch(Circle(c, R, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
def arcp(ax, c, r0, r1, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0) / 4)); pts = [pp(c, r0 + (r1 - r0) * i / n, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, pts, role, lw=lw)
    if head: arrow(ax, pts[-2], pts[-1], role, lw=lw)
def dot(ax, p, role, r=1.1): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))
TH = r'$\theta$'

fig, ax = canvas(64); c = (58, 32)
arrow(ax, (40, 32), (86, 32), 'fixe', lw=0.7); arrow(ax, (58, 8), (58, 58), 'fixe', lw=0.7)
ucirc(ax, c, 12); line(ax, [c, pp(c, 20, 40)], 'fixe'); arcp(ax, c, 6, 6, 0, 40, 'fixe', head=False)
dot(ax, c, 'sujet', 1.6)
text(ax, 62, 28, r'$O$', 'sujet', 'l'); text(ax, 74, 25, r'$(0\,;\,0)$', 'sujet', 's')
for y, s in ((54, 'centre du cercle unité'), (43, 'sommet des angles'), (11, 'axe du pédalier')):
    box(ax, 2, y - 4, 33, 8, 'fixe', label=s, size='s')
    arrow(ax, (35.8, y), (56.5, 32), 'fixe', lw=0.8)
save(fig, '28-040')
