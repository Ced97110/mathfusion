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

fig, ax = canvas(46)
O = (14, 22)
arrow(ax, (4, 22), (84, 22), 'fixe', lw=0.7)
line(ax, [O, (70, 22)], 'sujet', lw=2.6)
dot(ax, O, 'encre', 1.0); dot(ax, (70, 22), 'encre', 1.0)
text(ax, 14, 17.5, r'$O$'); text(ax, 70, 17.5, r'$A$')
text(ax, 42, 30, 'en français : demi-droite $OA$', 'sujet', 's')
brace(ax, 14, 70, 14, 'autre', down=True, depth=2.0)
text(ax, 42, 4, 'en anglais : axe polaire', 'autre', 's')
text(ax, 42, 39, 'une seule demi-droite, deux noms', 'encre', 's')
save(fig, '28-027')
