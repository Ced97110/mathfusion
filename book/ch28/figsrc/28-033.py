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

fig, ax = canvas(74); c = (30, 33); R = 25
ucirc(ax, c, R); axes_xy(ax, c, R)
line(ax, [c, pp(c, R, 50)], 'sujet', lw=1.6); dot(ax, pp(c, R, 50), 'sujet')
arcp(ax, c, 7, 7, 0, 50, 'varie'); arcp(ax, c, 11, 15, 0, 410, 'autre'); arcp(ax, c, 19, 22.5, 0, -310, 'encre')
text(ax, 54, 56, r'$P$', 'sujet', 'm'); text(ax, 33, 29.5, r'$O$', 'encre', 's')
text(ax, 62, 45, 'même côté\nfinal', 'sujet', 's')
text(ax, 12, 68, '50°', 'varie', 'm'); text(ax, 40, 68, '410°', 'autre', 'm'); text(ax, 68, 68, '−310°', 'encre', 'm')
save(fig, '28-033')
