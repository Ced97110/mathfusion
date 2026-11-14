import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(c, r, a): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0)/3)); pts = [pt(c, r, a0 + (a1 - a0)*i/n) for i in range(n + 1)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw)
def axes(ax, c, hx, hy, role='fixe'):
    arrow(ax, (c[0]-hx, c[1]), (c[0]+hx, c[1]), role, 0.7); arrow(ax, (c[0], c[1]-hy), (c[0], c[1]+hy), role, 0.7)
def dot(ax, p, role, r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(60)
c = (26, 30); s = 1.4
M = (c[0] - 14.72*s, c[1] - 8.5*s)
axes(ax, c, 22, 22)
line(ax, [c, M], 'sujet', 1.2); line(ax, [M, (M[0], c[1])], 'varie', 0.8, dash=True); line(ax, [M, (c[0], M[1])], 'varie', 0.8, dash=True)
arc(ax, c, 6, 0, 210, 'varie', 0.9); text(ax, 34, 38, '210°', 'varie', 's')
dot(ax, M, 'resultat', 1.1); text(ax, M[0] + 2, M[1] - 3, r'$M$', 'resultat', 's')
text(ax, M[0] + 1, c[1] + 3, '−14,72', 'varie', 's'); text(ax, c[0] + 9, M[1], '−8,5', 'varie', 's')
text(ax, 68, 50, r'$r = 17$', 'sujet', 'm'); text(ax, 68, 42, r'$\cos 210° \approx -0{,}866$', 'sujet', 's'); text(ax, 68, 36, r'$\sin 210° = -0{,}5$', 'sujet', 's')
text(ax, 68, 27, r'$17 \times (-0{,}866)$', 'varie', 's'); text(ax, 68, 21, r'$17 \times (-0{,}5)$', 'varie', 's')
text(ax, 68, 11, r'$M = (r\cos\theta, r\sin\theta)$', 'resultat', 's')
save(fig, '28-058')
