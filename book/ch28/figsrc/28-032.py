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

fig, ax = canvas(50)
f = numberline(ax, 4, 80, 18, -360, 450, 90, labels=False, arrow_right=False)
for v, role, s in ((-310, 'autre', '−310°'), (50, 'sujet', '50°'), (410, 'resultat', '410°')):
    dot(ax, (f(v), 18), role, 1.4); text(ax, f(v), 10, s, role, 'm')
arrow(ax, (f(50), 21), (f(410), 21), 'varie', curve=-0.45)
arrow(ax, (f(50), 21), (f(-310), 21), 'varie', curve=0.45)
text(ax, f(230), 37, '+ 360° (un tour)', 'varie', 's')
text(ax, f(-130), 37, '− 360° (un tour)', 'varie', 's')
text(ax, 44, 3, 'trois mesures, même arrivée', 'encre', 's')
save(fig, '28-032')
