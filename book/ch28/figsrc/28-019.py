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

fig, ax = canvas(66)
O = (60, 18); P = pt(O, 30, 130); N = (P[0], O[1])
axes(ax, O, 46, 14)
poly(ax, [O, N, P], 'sujet')
ray(ax, O, 130, 30, 'sujet', lw=1.2)
line(ax, [N, P], 'sujet', lw=1.2)
line(ax, [O, N], 'sujet', lw=1.2)
q = 3.2
line(ax, [(N[0] + q, N[1]), (N[0] + q, N[1] + q), (N[0], N[1] + q)], 'encre', lw=0.7)
arcp(ax, O, 9, 130, 180, 'sujet', lw=1.0, head=False)
text(ax, O[0] - 12, O[1] + 7, r'$50°$', 'sujet', 'm')
arcp(ax, O, 15, 0, 130, 'autre', lw=1.0)
text(ax, O[0] + 20, O[1] + 14, r'$\theta = 130°$', 'autre', 'm')
for p, s, d in ((O, 'O', (3, -3)), (N, 'N', (-2, -3)), (P, 'P', (3, 2.5))):
    dot(ax, p, 'encre', 0.9); text(ax, p[0] + d[0], p[1] + d[1], r'$%s$' % s)
text(ax, 22, 52, 'triangle rectangle $ONP$', 'sujet', 's', ha='left')
text(ax, 22, 47, 'angle droit en $N$', 'encre', 's', ha='left')
save(fig, '28-019')
