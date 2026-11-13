import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pt(o, r, a):
    return (o[0] + r * math.cos(math.radians(a)), o[1] + r * math.sin(math.radians(a)))
def arcp(ax, o, r, a0, a1, role, lw=1.0, head=True, dash=False):
    n = 60
    ps = [pt(o, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    line(ax, ps[:-1] if head else ps, role, lw=lw, dash=dash)
    if head: arrow(ax, ps[-3], ps[-1], role, lw=lw)
def ray(ax, o, a, L, role, lw=1.0, dash=False):
    line(ax, [o, pt(o, L, a)], role, lw=lw, dash=dash)
def axes(ax, o, lx, ly, role='fixe'):
    arrow(ax, (o[0] - lx, o[1]), (o[0] + lx, o[1]), role, lw=0.7)
    arrow(ax, (o[0], o[1] - ly), (o[0], o[1] + ly), role, lw=0.7)
def dot(ax, p, role, r=1.0):
    ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=6))

fig, ax = canvas(62)
O = (46, 22); P = pt(O, 24, 130); N = (P[0], O[1])
axes(ax, O, 40, 14)
ray(ax, O, 130, 24, 'fixe', dash=True)
line(ax, [O, N], 'varie', lw=2.2)
line(ax, [N, P], 'sujet', lw=2.2)
for p in (O, N, P): dot(ax, p, 'encre', 0.9)
text(ax, O[0] + 3, O[1] - 3, r'$O$'); text(ax, N[0] - 2, N[1] - 3, r'$N$'); text(ax, P[0] + 3, P[1] + 2.5, r'$P$')
text(ax, (O[0] + N[0]) / 2, O[1] - 8, r'$ON = x$ : à gauche de $O$', 'varie', 's')
text(ax, (O[0] + N[0]) / 2, O[1] - 13, r'donc $x$ est négative', 'varie', 's')
text(ax, N[0] - 3, (N[1] + P[1]) / 2, r'$NP = y$', 'sujet', 'm', ha='right')
text(ax, N[0] - 3, (N[1] + P[1]) / 2 - 5, 'hauteur de $P$', 'sujet', 's', ha='right')
save(fig, '28-017')
