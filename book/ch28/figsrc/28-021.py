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
O = (14, 14)
ray(ax, O, 0, 62, 'fixe', lw=1.8); ray(ax, O, 55, 46, 'resultat', lw=1.8)
arcp(ax, O, 16, 0, 55, 'varie', lw=1.2)
dot(ax, O, 'encre', 1.0)
text(ax, 50, 8, 'côté initial', 'fixe', 'm')
text(ax, 62, 56, 'côté final', 'resultat', 'm')
text(ax, 40, 31, 'rotation :', 'varie', 'm'); text(ax, 40, 26.5, 'sens et grandeur', 'varie', 's')
arrow(ax, (31, 29), (pt(O, 17, 30)[0] + 1.5, pt(O, 17, 30)[1] + 1.5), 'varie', lw=0.7)
text(ax, 14, 7, 'sommet', 'encre', 's')
text(ax, 20, 58, 'angle orienté = 3 données', 'sujet', 'm')
save(fig, '28-021')
