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

fig, ax = canvas(56)
O = (22, 28)
ray(ax, O, 20, 50, 'fixe', lw=1.6); ray(ax, O, 80, 22, 'fixe', lw=1.6)
ray(ax, O, 20, 50, 'fixe', lw=1.6)
disc(ax, O[0], O[1], 2.4, 'sujet')
text(ax, 6, 42, 'sommet', 'sujet', 'l', ha='left')
text(ax, 6, 36.5, 'point commun', 'sujet', 's', ha='left')
text(ax, 62, 18, 'côté initial', 'fixe', 'm')
text(ax, 38, 52, 'côté final', 'fixe', 'm')
arrow(ax, (12, 34), (O[0] - 1.8, O[1] + 1.4), 'sujet', lw=0.8)
save(fig, '28-025')
