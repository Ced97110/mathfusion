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

fig, ax = canvas(88)
O = (34, 40)
ray(ax, O, 0, 40, 'fixe', lw=1.0, dash=True)
ray(ax, O, 50, 36, 'encre', lw=1.4)
arcp(ax, O, 9, 0, 50, 'sujet', lw=1.6)
n = 100
sp = [pt(O, 14 + 4 * i / n, 410 * i / n) for i in range(n + 1)]
line(ax, sp[:-1], 'resultat', lw=1.6); arrow(ax, sp[-4], sp[-1], 'resultat', lw=1.6)
arcp(ax, O, 24, 0, -310, 'autre', lw=1.6)
dot(ax, O, 'encre', 0.9)
text(ax, O[0] - 3, O[1] - 3, r'$O$'); text(ax, pt(O, 39, 50)[0] + 2, pt(O, 39, 50)[1] + 2, r'$P$', 'encre', 'l')
text(ax, 76, 32, 'départ', 'fixe', 's')
text(ax, 62, 50, '50°', 'sujet', 'm')
text(ax, 6, 62, '410°', 'resultat', 'm', ha='left'); text(ax, 6, 57, '= 360° + 50°', 'resultat', 's', ha='left')
text(ax, 6, 12, '−310°', 'autre', 'm', ha='left'); text(ax, 6, 7, 'à l’envers', 'autre', 's', ha='left')
text(ax, 62, 78, 'même arrivée', 'encre', 'm')
save(fig, '28-031')
