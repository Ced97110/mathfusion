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

fig, ax = canvas(68)
O = (34, 30)
poly(ax, [O, (O[0] + 28, O[1]), (O[0] + 28, O[1] + 28), (O[0], O[1] + 28)], 'resultat')
axes(ax, O, 32, 30)
arcp(ax, O, 18, 0, 90, 'varie', lw=1.8)
dot(ax, O, 'encre', 0.9)
text(ax, O[0] + 12, O[1] + 4, '90°', 'varie', 'm')
text(ax, 80, 33, r'$x$ positifs', 'fixe', 's', ha='right')
text(ax, O[0] + 3, 61, r'$y$ positifs', 'fixe', 's', ha='left')
text(ax, O[0] + 17, O[1] + 20, 'quadrant I', 'resultat', 'm')
text(ax, O[0] + 17, O[1] + 15, '$x$ et $y$ > 0', 'resultat', 's')
text(ax, 4, 4, 'départ : axe des $x$ positifs', 'encre', 's', ha='left')
text(ax, 4, 9, 'arrivée : axe des $y$ positifs', 'encre', 's', ha='left')
save(fig, '28-030')
