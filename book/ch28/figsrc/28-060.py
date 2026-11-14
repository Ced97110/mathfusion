import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(c, r, a): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0)/3)); pts = [pt(c, r, a0 + (a1 - a0)*i/n) for i in range(n + 1)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw)
def axes(ax, c, hx, hy, role='fixe'):
    arrow(ax, (c[0]-hx, c[1]), (c[0]+hx, c[1]), role, 0.7); arrow(ax, (c[0], c[1]-hy), (c[0], c[1]+hy), role, 0.7)
def dot(ax, p, role, r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(52)
c = (44, 10); s = 5
M = (c[0] - 3*s, c[1] + 4*s); N = (M[0], c[1])
arrow(ax, (c[0] - 26, c[1]), (c[0] + 12, c[1]), 'fixe', 0.7); arrow(ax, (c[0], c[1] - 3), (c[0], c[1] + 30), 'fixe', 0.7)
poly(ax, [c, N, M], 'fixe'); line(ax, [c, M], 'sujet', 1.5); line(ax, [c, N], 'varie', 1.8)
arc(ax, c, 6, 0, 127, 'fixe', 0.8, head=False); text(ax, 49, 16.5, r'$\theta$', 'fixe', 's')
dot(ax, M, 'sujet', 1.1); text(ax, M[0] - 2.5, M[1] + 2.5, r'$M$', 'sujet', 's')
text(ax, (c[0] + N[0])/2, 5.5, r'$x = -3$', 'varie', 's'); text(ax, 41, 25, r'$r = 5$', 'sujet', 's')
text(ax, 71, 40, r'$\cos\theta = x \div r$', 'resultat', 'm'); text(ax, 71, 32, r'$= -3 \div 5$', 'resultat', 'm'); text(ax, 71, 24, r'$= -0{,}6$', 'resultat', 'm')
save(fig, '28-060')
