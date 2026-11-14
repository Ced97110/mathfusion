import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(c, r, a): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role, lw=1.0, head=True):
    n = max(8, int(abs(a1 - a0)/3)); pts = [pt(c, r, a0 + (a1 - a0)*i/n) for i in range(n + 1)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-3], pts[-1], role, lw)
def axes(ax, c, hx, hy, role='fixe'):
    arrow(ax, (c[0]-hx, c[1]), (c[0]+hx, c[1]), role, 0.7); arrow(ax, (c[0], c[1]-hy), (c[0], c[1]+hy), role, 0.7)
def dot(ax, p, role, r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))
fig, ax = canvas(64)
text(ax, 44, 60, 'même angle : 30°', 'encre', 'm')
box(ax, 4, 42, 32, 10, 'autre', label='ancienne définition', size='s'); box(ax, 52, 42, 32, 10, 'sujet', label='nouvelle définition', size='s')
arrow(ax, (20, 41.5), (20, 30.5), 'encre'); arrow(ax, (68, 41.5), (68, 30.5), 'encre')
text(ax, 24, 35.6, r'$\sin$', 'encre', 's'); text(ax, 72, 35.6, r'$\sin$', 'encre', 's')
box(ax, 8, 19, 24, 11, 'resultat', label='0,5', size='l'); box(ax, 56, 19, 24, 11, 'resultat', label='0,5', size='l')
text(ax, 44, 24.5, '=', 'resultat', 'xl', weight='bold')
box(ax, 14, 3, 60, 9, 'limite', dash=True, label='si 0,6 : deux sinus', size='s')
text(ax, 44, 15.5, 'sinon', 'limite', 's')
save(fig, '28-053')
