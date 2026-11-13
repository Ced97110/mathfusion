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
O = (10, 8); R = 40; P = pt(O, R, 30); N = (P[0], O[1])
arc(ax, O, R, 0, 90, 'fixe', head=False); axes(ax, O, 0.01, 0.01)
arrow(ax, (O[0] - 3, O[1]), (O[0] + R + 4, O[1]), 'fixe', 0.7); arrow(ax, (O[0], O[1] - 3), (O[0], O[1] + R + 4), 'fixe', 0.7)
poly(ax, [O, N, P], 'sujet'); line(ax, [O, P], 'varie', 1.4)
line(ax, [(N[0] - 2, O[1]), (N[0] - 2, O[1] + 2), (N[0], O[1] + 2)], 'sujet', 0.6)
arc(ax, O, 12, 0, 30, 'sujet', head=False); text(ax, 26, 11.8, '30°', 'sujet', 's')
dot(ax, P, 'varie'); text(ax, P[0] + 2.5, P[1] + 2.5, r'$P$', 'varie', 's'); text(ax, 7, 5, r'$O$', 'encre', 's'); text(ax, N[0] + 1, 4.8, r'$N$', 'encre', 's')
text(ax, 24, 21.5, '1', 'varie', 's'); text(ax, N[0] + 4.5, 18, '0,5', 'sujet', 's'); text(ax, 27, 4.8, '0,866', 'sujet', 's')
text(ax, 71, 47, 'ancienne définition', 'encre', 's')
text(ax, 71, 38, r'$NP \div OP$', 'sujet', 'm'); text(ax, 71, 31, r'$= y \div 1$', 'resultat', 'm'); text(ax, 71, 24, r'$= y$', 'resultat', 'm')
text(ax, 71, 16, 'car OP = 1', 'varie', 's')
save(fig, '28-054')
