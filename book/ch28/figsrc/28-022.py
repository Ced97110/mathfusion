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

fig, ax = canvas(52)
O = (14, 14)
ray(ax, O, 0, 62, 'sujet', lw=2.6); arrow(ax, (72, 14), (79, 14), 'sujet', lw=2.6)
ray(ax, O, 45, 34, 'fixe', lw=0.9, dash=True)
arcp(ax, O, 16, 0, 45, 'varie', lw=0.9)
dot(ax, O, 'encre', 1.2)
text(ax, 14, 6, 'début', 'encre', 's')
text(ax, 46, 8, 'côté initial', 'sujet', 'l')
text(ax, 46, 20, 'demi-droite de départ', 'sujet', 's')
text(ax, 42, 43, 'ce qu’on tourne', 'fixe', 's')
text(ax, 42, 38, 'ensuite', 'fixe', 's')
save(fig, '28-022')
