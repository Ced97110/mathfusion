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

fig, ax = canvas(70)
O = (30, 24)
ray(ax, O, 0, 40, 'fixe', lw=1.2, dash=True); ray(ax, O, 130, 36, 'sujet', lw=1.8)
arcp(ax, O, 18, 0, 130, 'varie', lw=1.6)
arcp(ax, O, 11, 0, 130, 'varie', lw=0.6, head=False, dash=True)
dot(ax, O, 'encre', 1.0)
text(ax, 70, 19, 'départ', 'fixe', 's')
text(ax, 18, 62, 'arrivée', 'sujet', 's')
text(ax, 62, 46, 'sens : flèche', 'varie', 's'); text(ax, 62, 41, 'de départ à arrivée', 'varie', 's')
arrow(ax, (50, 44), (pt(O, 19, 70)[0] + 2, pt(O, 19, 70)[1]), 'varie', lw=0.7)
text(ax, 62, 12, 'grandeur : 130°', 'varie', 'm')
save(fig, '28-024')
