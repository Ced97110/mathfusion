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
xs = [11, 33, 55, 77]; roles = ['sujet', 'varie', 'sujet', 'resultat']
titles = ['angle', 'rotation', 'point', 'coordonnées']; caps = ['nombre', 'geste', 'position', 'deux nombres']
for i, (x, r) in enumerate(zip(xs, roles)):
    box(ax, x - 9, 14, 18, 24, r)
    text(ax, x, 44, titles[i], r, 's', weight='bold'); text(ax, x, 8, caps[i], r, 's')
    if i < 3: arrow(ax, (x + 9.4, 26), (xs[i + 1] - 9.4, 26), 'encre', 0.9)
text(ax, xs[0], 26, '130°', 'sujet', 'l', weight='bold')
c = (xs[1], 26); disc(ax, *c, 6, 'fixe', fill=False); line(ax, [c, (c[0] + 8, c[1])], 'fixe', dash=True); arc(ax, c, 4, 0, 130, 'varie', 1.1)
c = (xs[2], 26); disc(ax, *c, 6, 'fixe', fill=False); P = pt(c, 6, 130); dot(ax, P, 'sujet', 1.2); text(ax, P[0] - 2.2, P[1] + 2.4, r'$P$', 'sujet', 's')
text(ax, xs[3], 31, r'$x$', 'resultat', 'l'); text(ax, xs[3], 21, r'$y$', 'resultat', 'l')
save(fig, '28-052')
