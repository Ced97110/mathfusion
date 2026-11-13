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

fig, ax = canvas(54)
O = (44, 14)
ray(ax, O, 25, 36, 'fixe', lw=1.4); ray(ax, O, 155, 36, 'fixe', lw=1.4)
arcp(ax, O, 14, 25, 155, 'varie', lw=1.0, head=False)
arrow(ax, pt(O, 14, 27), pt(O, 14, 23), 'varie', lw=1.0)
arrow(ax, pt(O, 14, 153), pt(O, 14, 157), 'varie', lw=1.0)
text(ax, 44, 35, 'ouverture : 130°', 'varie', 'm')
dot(ax, O, 'encre', 0.9)
text(ax, 72, 38, 'départ ?', 'fixe', 'm')
text(ax, 16, 38, 'arrivée ?', 'fixe', 'm')
text(ax, 44, 5, 'quel sens ? combien de tours ?', 'fixe', 's')
save(fig, '28-020')
