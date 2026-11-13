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
text(ax, 22, 51, 'avant', 'fixe', 'l', weight='bold'); text(ax, 64, 51, 'après', 'sujet', 'l', weight='bold')
O = (6, 20); a = math.radians(30); L = 30
A = (O[0] + L*math.cos(a), O[1]); B = (A[0], O[1] + L*math.sin(a))
poly(ax, [O, A, B], 'fixe'); arc(ax, O, 8, 0, 30, 'fixe', head=False); text(ax, 18, 22.4, r'$30°$', 'fixe', 's')
text(ax, 22, 11, 'coin d’un triangle', 'fixe', 's'); text(ax, 22, 6.5, 'de 0° à 90°', 'fixe', 's')
c = (64, 28)
disc(ax, *c, 10, 'fixe', fill=False); line(ax, [c, (c[0] + 14, c[1])], 'fixe', dash=True)
arc(ax, c, 13, 0, 130, 'sujet', 1.2); arc(ax, c, 17, 0, -310, 'varie', 1.2)
text(ax, c[0], c[1] + 2.4, '+130°', 'sujet', 's'); text(ax, c[0], c[1] - 2.4, '−310°', 'varie', 's')
text(ax, 66, 6, 'nombre de rotation, signé', 'sujet', 's')
save(fig, '28-049')
