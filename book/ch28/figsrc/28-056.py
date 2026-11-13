import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(c, r, a): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0)/3)); pts = [pt(c, r, a0 + (a1 - a0)*i/n) for i in range(n + 1)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw)
def axes(ax, c, hx, hy, role='fixe'):
    arrow(ax, (c[0]-hx, c[1]), (c[0]+hx, c[1]), role, 0.7); arrow(ax, (c[0], c[1]-hy), (c[0], c[1]+hy), role, 0.7)
def dot(ax, p, role, r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(56)
c = (44, 28); R = 22
disc(ax, *c, R, 'fixe', fill=False); axes(ax, c, R + 4, R + 4)
P30 = pt(c, R, 30); poly(ax, [c, (P30[0], c[1]), P30], 'sujet'); dot(ax, P30, 'sujet')
P = pt(c, R, 130); line(ax, [c, P], 'varie', 1.3); dot(ax, P, 'varie', 1.1)
line(ax, [P, (P[0], c[1])], 'varie', 0.8, dash=True); line(ax, [P, (c[0], P[1])], 'varie', 0.8, dash=True)
arc(ax, c, 8, 0, 130, 'varie', 0.9)
text(ax, P[0] - 2.5, P[1] + 2.5, r'$P$', 'varie', 's'); text(ax, P[0], c[1] - 2.5, r'$x$', 'varie', 's'); text(ax, c[0] + 2.5, P[1] + 0.5, r'$y$', 'varie', 's')
text(ax, 15, 15, '130° :', 'varie', 's'); text(ax, 15, 11, 'pas de triangle,', 'varie', 's'); text(ax, 15, 7, 'mais x et y', 'varie', 's')
text(ax, 73, 15, '30° :', 'sujet', 's'); text(ax, 73, 11, 'triangle', 'sujet', 's')
save(fig, '28-056')
