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

fig, ax = canvas(72); c = (44, 36); R = 24
ucirc(ax, c, R); axes_xy(ax, c, R)
for a, r0, r1 in ((30, 7, 7), (130, 11, 11), (410, 15, 19)):
    pass
for a, r0, r1, role in ((30, 7, 7, 'varie'), (130, 11, 11, 'autre'), (410, 14, 18, 'encre')):
    arcp(ax, c, r0, r1, 0, a, role); line(ax, [c, pp(c, R, a)], 'fixe', dash=True); dot(ax, pp(c, R, a), role, 0.9)
dot(ax, pp(c, R, 0), 'sujet', 1.5)
text(ax, 69, 31, r'$A(1\,;\,0)$', 'sujet', 's', ha='center'); text(ax, 40, 32, r'$O$', 'encre', 's')
text(ax, pp(c, R + 6, 30)[0] + 1, pp(c, R + 6, 30)[1] + 1, '30°', 'varie', 's')
text(ax, pp(c, R + 6, 130)[0] - 1, pp(c, R + 6, 130)[1] + 2, '130°', 'autre', 's')
text(ax, pp(c, R + 6, 50)[0] + 1, pp(c, R + 6, 50)[1] + 2, '410°', 'encre', 's')
text(ax, 44, 68, 'même départ : le point A', 'sujet', 's')
save(fig, '28-041')
