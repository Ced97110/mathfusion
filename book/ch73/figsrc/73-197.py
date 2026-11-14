import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))
def arc(ax, c, r, a0, a1, role, lw=1.1, head=True):
    pts = [P(c, r, a0 + (a1 - a0) * i / 40) for i in range(41)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-4], pts[-1], role, lw)

fig, ax = canvas(72)
o = (12, 10); k = 8.0
arrow(ax, o, (o[0] + 70, o[1]), 'fixe', lw=0.8); arrow(ax, o, (o[0], o[1] + 56), 'fixe', lw=0.8)
text(ax, 80, 6, 'x', 'fixe', 's'); text(ax, 6, 64, 'y', 'fixe', 's')
xs = [2.0 + i * 0.05 for i in range(0, 101)]
line(ax, [(o[0] + x * k, o[1] + 12 / x * k) for x in xs], 'sujet', lw=1.3)
p = (o[0] + 3 * k, o[1] + 4 * k); q = (o[0] + 6 * k, o[1] + 2 * k)
dot(ax, p, 'sujet', 1.8); dot(ax, q, 'resultat', 1.8)
arrow(ax, (p[0] + 3, p[1] + 1), (q[0] - 3, q[1] + 2), 'varie', curve=-0.3)
text(ax, p[0] + 3, p[1] + 7, '(3, 4) : 3 × 4 = 12', 'sujet', 's', ha='left')
text(ax, q[0] + 4, q[1] - 6, '(6, 2) : 6 × 2 = 12', 'resultat', 's')
text(ax, 62, 52, r'$(x,\,y)\mapsto(2x,\,y/2)$', 'varie', 's')
text(ax, 62, 62, 'forme  Q = xy', 'sujet', 's')
save(fig, '73-197')
