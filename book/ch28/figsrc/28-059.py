import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(c, r, a): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0)/3)); pts = [pt(c, r, a0 + (a1 - a0)*i/n) for i in range(n + 1)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw)
def axes(ax, c, hx, hy, role='fixe'):
    arrow(ax, (c[0]-hx, c[1]), (c[0]+hx, c[1]), role, 0.7); arrow(ax, (c[0], c[1]-hy), (c[0], c[1]+hy), role, 0.7)
def dot(ax, p, role, r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(58)
s = 4; O = (22, 24); A = (O[0] + 3*s, O[1]); M = (A[0], O[1] + 4*s)
nrm = (-4*s, 3*s)
poly(ax, [O, A, (A[0], A[1] - 3*s), (O[0], O[1] - 3*s)], 'fixe')
poly(ax, [A, M, (M[0] + 4*s, M[1]), (A[0] + 4*s, A[1])], 'fixe')
poly(ax, [O, M, (M[0] + nrm[0], M[1] + nrm[1]), (O[0] + nrm[0], O[1] + nrm[1])], 'resultat')
poly(ax, [O, A, M], 'sujet'); line(ax, [O, M], 'varie', 1.6)
text(ax, 28, 18, '9', 'fixe', 'l'); text(ax, 42, 32, '16', 'fixe', 'l'); text(ax, 20, 38, '25', 'resultat', 'l')
text(ax, 28, 26.4, '3', 'sujet', 's'); text(ax, 31.4, 32, '4', 'sujet', 's')
text(ax, 36.5, 43.5, r'$M$', 'sujet', 's'); text(ax, 20.5, 21.5, r'$O$', 'encre', 's')
text(ax, 71, 40, r'$9 + 16 = 25$', 'resultat', 'm'); text(ax, 71, 31, r'$r = \sqrt{25} = 5$', 'varie', 'm')
save(fig, '28-059')
