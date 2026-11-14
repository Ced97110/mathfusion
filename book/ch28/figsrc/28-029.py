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

fig, ax = canvas(64)
O = (30, 32)
axes(ax, O, 26, 22)
ray(ax, O, 0, 22, 'fixe', lw=1.4); ray(ax, O, -50, 22, 'sujet', lw=1.8)
arcp(ax, O, 14, 0, -50, 'varie', lw=1.6)
dot(ax, O, 'encre', 0.9)
text(ax, 66, 44, 'sens des aiguilles', 'varie', 'm'); text(ax, 66, 39, 'd’une montre', 'varie', 'm')
arrow(ax, (58, 36), (pt(O, 15, -15)[0] + 1.5, pt(O, 15, -15)[1] + 1), 'varie', lw=0.7)
text(ax, 62, 14, 'angle négatif', 'resultat', 'l'); text(ax, 62, 8, '− 50°', 'resultat', 'l')
text(ax, 54, 27, 'départ', 'fixe', 's')
save(fig, '28-029')
