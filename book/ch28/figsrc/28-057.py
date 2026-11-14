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
O = (6, 8); u = 14; k = 3
P = pt(O, u, 30); M = pt(O, k*u, 30)
poly(ax, [O, (M[0], O[1]), M], 'autre'); poly(ax, [O, (P[0], O[1]), P], 'sujet')
line(ax, [O, M], 'varie', 1.2)
dot(ax, P, 'sujet'); dot(ax, M, 'autre')
text(ax, P[0] - 2, P[1] + 3, r'$P$', 'sujet', 's'); text(ax, M[0] + 2.5, M[1] + 2.5, r'$M$', 'autre', 's'); text(ax, O[0] - 1, O[1] - 3, r'$O$', 'encre', 's')
box(ax, 52, 36, 32, 9, 'sujet', label='triangle ONP', size='s'); box(ax, 52, 17, 32, 9, 'autre', label='triangle de M', size='s')
arrow(ax, (68, 35.6), (68, 26.4), 'varie', 1.2); text(ax, 74, 31, r'$\times r$', 'varie', 's')
text(ax, 68, 11, r'$r = 17$ : 14,72 et 8,5', 'autre', 's')
save(fig, '28-057')
