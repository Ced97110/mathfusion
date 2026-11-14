import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(c, r, a): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0)/3)); pts = [pt(c, r, a0 + (a1 - a0)*i/n) for i in range(n + 1)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw)
def axes(ax, c, hx, hy, role='fixe'):
    arrow(ax, (c[0]-hx, c[1]), (c[0]+hx, c[1]), role, 0.7); arrow(ax, (c[0], c[1]-hy), (c[0], c[1]+hy), role, 0.7)
def dot(ax, p, role, r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(46)
O = (8, 6); u = 14
arrow(ax, (O[0], O[1] - 1), (O[0], O[1] + 36), 'fixe', 0.7); arrow(ax, (O[0] - 1, O[1]), (O[0] + 30, O[1]), 'fixe', 0.7)
arc(ax, O, 2*u, 0, 60, 'autre', head=False); arc(ax, O, u, 0, 60, 'sujet', head=False)
P2 = pt(O, 2*u, 30); P1 = pt(O, u, 30)
line(ax, [O, P2], 'fixe', 0.7, dash=True)
line(ax, [P2, (O[0], P2[1])], 'autre', 0.9, dash=True); line(ax, [P1, (O[0], P1[1])], 'sujet', 0.9, dash=True)
dot(ax, P2, 'autre'); dot(ax, P1, 'sujet')
text(ax, 4, P2[1], '1', 'autre', 's'); text(ax, 3.5, P1[1] - 1, '0,5', 'sujet', 's')
box(ax, 44, 33, 42, 9, 'autre', label='rayon 2 : hauteur 1', size='s'); text(ax, 65, 28.5, r'$1 \div 2 = 0{,}5$', 'autre', 's')
box(ax, 44, 15, 42, 9, 'sujet', label='rayon 1 : hauteur 0,5', size='s'); text(ax, 65, 10.5, 'division par 1 : rien à faire', 'resultat', 's')
save(fig, '28-055')
