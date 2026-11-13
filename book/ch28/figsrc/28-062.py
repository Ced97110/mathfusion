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
O = (46, 8); s = 4
M = (O[0] - 6*s, O[1] + 8*s); P = (O[0] - 0.6*s, O[1] + 0.8*s)
arrow(ax, (30, O[1]), (58, O[1]), 'fixe', 0.7); arrow(ax, (O[0], O[1] - 1), (O[0], O[1] + 38), 'fixe', 0.7)
line(ax, [O, M], 'fixe', 0.8, dash=True); disc(ax, *O, s, 'sujet', fill=False, lw=1.2)
arrow(ax, (M[0] + 1.5, M[1] - 2), (P[0] - 0.6, P[1] + 0.8), 'varie', 1.2)
dot(ax, M, 'autre', 1.1); dot(ax, P, 'resultat', 0.9)
text(ax, 22, 45, r'$M(-6 ; 8)$', 'autre', 's'); text(ax, 38, 27, '÷ 10', 'varie', 'm')
text(ax, 56, 14.5, 'rayon 1', 'sujet', 's')
text(ax, 72, 24, r'$(-0{,}6 ; 0{,}8)$', 'resultat', 'm'); text(ax, 72, 19, r'$=(\cos\theta ; \sin\theta)$', 'resultat', 's')
save(fig, '28-062')
