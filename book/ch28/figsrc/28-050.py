import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(c, r, a): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0)/3)); pts = [pt(c, r, a0 + (a1 - a0)*i/n) for i in range(n + 1)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw)
def axes(ax, c, hx, hy, role='fixe'):
    arrow(ax, (c[0]-hx, c[1]), (c[0]+hx, c[1]), role, 0.7); arrow(ax, (c[0], c[1]-hy), (c[0], c[1]+hy), role, 0.7)
def dot(ax, p, role, r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(66)
c = (44, 36); R = 20
disc(ax, *c, R, 'fixe', fill=False); axes(ax, c, R + 5, R + 5)
P = pt(c, R, 130); N = (P[0], c[1])
poly(ax, [c, N, P], 'fixe')
line(ax, [c, N], 'sujet', 1.8); line(ax, [N, P], 'autre', 1.8)
arc(ax, c, 6, 0, 130, 'varie', 0.9)
dot(ax, P, 'encre'); text(ax, P[0] - 2.5, P[1] + 2.5, r'$P$', 'encre', 's')
text(ax, 54, 41, '130°', 'varie', 's')
text(ax, 20, 33, '−', 'sujet', 'l', weight='bold'); text(ax, 69, 33, '+', 'fixe', 'l', weight='bold')
text(ax, 37.5, 31, r'$\cos\theta$', 'sujet', 's'); text(ax, 37.5, 12, r'$\cos\theta$ : à gauche', 'sujet', 's')
text(ax, 37.5, 8, 'nombre négatif', 'sujet', 's'); text(ax, N[0] + 7, 50 - 6.5, r'$\sin\theta$', 'autre', 's')
save(fig, '28-050')
