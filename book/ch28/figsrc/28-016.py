import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, d): return (c[0] + r * math.cos(math.radians(d)), c[1] + r * math.sin(math.radians(d)))
def arc(ax, c, r, a0, a1, role, lw=0.9, dash=False, n=48): line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, p, role, r=1.0): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], lw=0.5, zorder=4))
def sq(ax, p, ux, uy, s=2.2, role='fixe'): line(ax, [(p[0] + ux * s, p[1]), (p[0] + ux * s, p[1] + uy * s), (p[0], p[1] + uy * s)], role, lw=0.7)

fig, ax = canvas(62)
for cx, ang, lab in [(22, 130, '130°'), (66, 30, '30°')]:
    O = (cx, 30); R = 16; P = pol(O, R, ang); N = (P[0], 30)
    line(ax, [(cx - 19, 30), (cx + 19, 30)], 'fixe', lw=0.7)
    arc(ax, O, R, 0, 360, 'fixe', lw=0.8, n=90)
    line(ax, [O, P], 'sujet', lw=1.0)
    line(ax, [O, N], 'varie', lw=2.0)
    line(ax, [N, P], 'resultat', lw=2.0)
    arc(ax, O, 5, 0, ang, 'varie', lw=0.8)
    dot(ax, O, 'fixe', 0.9); dot(ax, P, 'sujet', 1.2); dot(ax, N, 'varie', 1.4)
    text(ax, cx + 1.5, 26.5, r'$O$')
    text(ax, N[0], 25.5 if ang == 130 else 25.5, r'$N$', 'varie', weight='bold') if False else None
    text(ax, N[0] + (-2.5 if ang == 130 else 2.5), 26.5, r'$N$', 'varie', weight='bold')
    text(ax, P[0] + (-2.5 if ang == 130 else 2.5), P[1] + 3, r'$P$', 'sujet')
    text(ax, cx, 49, lab, 'varie')
text(ax, 22, 9, 'N à gauche de O', 'varie')
text(ax, 66, 9, 'N à droite de O', 'varie')
save(fig, '28-016')
