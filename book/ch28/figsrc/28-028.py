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
O = (30, 30)
axes(ax, O, 26, 22)
ray(ax, O, 0, 22, 'fixe', lw=1.4); ray(ax, O, 50, 22, 'sujet', lw=1.8)
arcp(ax, O, 14, 0, 50, 'varie', lw=1.6)
dot(ax, O, 'encre', 0.9)
text(ax, 66, 16, 'sens contraire', 'varie', 'm'); text(ax, 66, 11, 'des aiguilles', 'varie', 'm')
arrow(ax, (58, 20), (pt(O, 15, 12)[0] + 1, pt(O, 15, 12)[1] - 0.5), 'varie', lw=0.7)
text(ax, 62, 54, 'angle positif', 'resultat', 'l'); text(ax, 62, 48, '+ 50°', 'resultat', 'l')
text(ax, 4, 4, 'départ', 'fixe', 's', ha='left')
save(fig, '28-028')
