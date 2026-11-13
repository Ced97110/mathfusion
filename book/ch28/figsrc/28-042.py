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

fig, ax = canvas(66); R = 14
text(ax, 44, 61, r'$\theta$ : quantité tournée, avec son signe', 'sujet', 's')
c1 = (22, 34); c2 = (66, 34)
for c in (c1, c2):
    ucirc(ax, c, R); line(ax, [c, pp(c, R, 0)], 'fixe'); dot(ax, c, 'fixe', 0.8)
arcp(ax, c1, 8, 8, 0, 130, 'varie'); line(ax, [c1, pp(c1, R, 130)], 'sujet', lw=1.4)
arcp(ax, c2, 8, 8, 0, -310, 'varie'); line(ax, [c2, pp(c2, R, 50)], 'sujet', lw=1.4)
text(ax, 22, 14, r'$\theta$ = 130°', 'sujet', 'm'); text(ax, 66, 14, r'$\theta$ = −310°', 'sujet', 'm')
text(ax, 22, 6, 'sens contraire des\naiguilles : +', 'varie', 's'); text(ax, 66, 6, 'sens des aiguilles : −', 'varie', 's')
save(fig, '28-042')
