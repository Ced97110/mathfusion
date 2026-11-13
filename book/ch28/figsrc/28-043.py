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

fig, ax = canvas(70); c = (44, 35); R = 24
ucirc(ax, c, R); axes_xy(ax, c, R)
dot(ax, pp(c, R, 0), 'fixe', 1.3)
for a, r, lab in ((130, 8, '130°'), (210, 13, '210°')):
    arcp(ax, c, r, r, 0, a, 'varie'); line(ax, [c, pp(c, R, a)], 'fixe', dash=True); dot(ax, pp(c, R, a), 'sujet', 1.5)
text(ax, 69, 31.5, r'$A$', 'fixe', 'm'); text(ax, 47, 31.5, r'$O$', 'encre', 's')
p = pp(c, R, 130); text(ax, p[0] - 3, p[1] + 3, r'$P$', 'sujet', 'l'); p = pp(c, R, 210); text(ax, p[0] - 3, p[1] - 3, r'$P$', 'sujet', 'l')
text(ax, 13, 54, TH + ' = 130°', 'varie', 's', ha='left'); text(ax, 13, 17, TH + ' = 210°', 'varie', 's', ha='left')
text(ax, 62, 62, 'P : arrivée de A', 'sujet', 's')
save(fig, '28-043')
