import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(c, r, a): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0)/3)); pts = [pt(c, r, a0 + (a1 - a0)*i/n) for i in range(n + 1)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw)
def axes(ax, c, hx, hy, role='fixe'):
    arrow(ax, (c[0]-hx, c[1]), (c[0]+hx, c[1]), role, 0.7); arrow(ax, (c[0], c[1]-hy), (c[0], c[1]+hy), role, 0.7)
def dot(ax, p, role, r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(62)
c = (44, 29); R = 22
poly(ax, [c] + [pt(c, R, a) for a in range(180, 270, 4)] + [pt(c, R, 270)], 'sujet')
disc(ax, *c, R, 'fixe', fill=False); axes(ax, c, R + 4, R + 2)
P = pt(c, R, 210); line(ax, [c, P], 'sujet', 1.5); dot(ax, P, 'sujet', 1.1); arc(ax, c, 7, 0, 210, 'varie', 1.0)
for lab, a, r in zip(['+ ; +', '− ; +', '− ; −', '+ ; −'], [45, 135, 225, 315], ['fixe', 'fixe', 'sujet', 'fixe']):
    p = pt(c, 12, a); text(ax, p[0], p[1], lab, r, 's', weight='bold')
text(ax, 21.5, 20.5, r'$P$', 'sujet', 's'); text(ax, 22, 12, '210°', 'varie', 's')
text(ax, 78, 33, r'$\cos\theta = x$', 'fixe', 's'); text(ax, 60, 58, r'$\sin\theta = y$', 'fixe', 's')
text(ax, 44, 2.2, 'signes de (x ; y)', 'sujet', 'm')
save(fig, '28-064')
