import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, d): return (c[0] + r * math.cos(math.radians(d)), c[1] + r * math.sin(math.radians(d)))
def arc(ax, c, r, a0, a1, role, lw=0.9, dash=False, n=48): line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, p, role, r=1.0): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], lw=0.5, zorder=4))
def sq(ax, p, ux, uy, s=2.2, role='fixe'): line(ax, [(p[0] + ux * s, p[1]), (p[0] + ux * s, p[1] + uy * s), (p[0], p[1] + uy * s)], role, lw=0.7)

fig, ax = canvas(70)
O = (44, 36)
arc(ax, O, 28, 0, 360, 'fixe', lw=1.0, n=120)
arc(ax, O, 14, 0, 360, 'sujet', lw=1.4, n=90)
line(ax, [O, (58, 36)], 'sujet', lw=1.2)
line(ax, [O, pol(O, 28, 135)], 'fixe', lw=1.0)
dot(ax, O, 'sujet', 1.1)
text(ax, 40.5, 39.5, r'$O$', 'sujet')
text(ax, 51, 33, 'rayon 1', 'sujet', 's')
text(ax, 44, 28, 'cercle unité', 'sujet', weight='bold')
text(ax, 24, 58, 'rayon 2', 'fixe', ha='right')
text(ax, 44, 4, 'rayon 2 : pas un cercle unité', 'fixe', 's') if False else None
save(fig, '28-012')
