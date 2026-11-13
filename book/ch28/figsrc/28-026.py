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
L = (10, 22)
ray(ax, L, 20, 26, 'fixe', lw=1.2); ray(ax, L, 150, 26, 'fixe', lw=1.2)
arcp(ax, L, 9, 20, 150, 'fixe', lw=0.8)
text(ax, 22, 33, '130°', 'fixe', 's')
dot(ax, L, 'encre', 0.9)
text(ax, 22, 54, 'n’importe où', 'fixe', 'm')
text(ax, 22, 8, 'pas de coordonnées', 'fixe', 's')
line(ax, [(44, 4), (44, 58)], 'fixe', lw=0.5, dash=True)
O = (62, 22)
axes(ax, O, 20, 17)
ray(ax, O, 0, 16, 'sujet', lw=2.0); ray(ax, O, 130, 18, 'sujet', lw=1.2)
arcp(ax, O, 8, 0, 130, 'varie', lw=0.9)
text(ax, 71, 32, '130°', 'varie', 's')
dot(ax, O, 'encre', 0.9); dot(ax, (O[0] + 16, O[1]), 'encre', 0.9)
text(ax, O[0] - 3, O[1] - 3, r'$O$'); text(ax, O[0] + 16, O[1] - 3.5, r'$A\,(1,\,0)$', 'sujet', 's')
text(ax, 66, 54, 'position standard', 'sujet', 'm')
text(ax, 62, 8, 'sommet en $O$, départ $OA$', 'sujet', 's')
save(fig, '28-026')
