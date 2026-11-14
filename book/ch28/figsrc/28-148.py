import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pt(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arc(ax, cx, cy, r, a0, a1, role, head=False, lw=0.9, dash=False):
    pts = [pt(cx, cy, r, a0 + (a1 - a0) * i / 120) for i in range(121)]
    line(ax, pts, role, lw=lw, dash=dash)
    if head: arrow(ax, pt(cx, cy, r, a1 - (a1 - a0) * 0.05), pts[-1], role, lw=lw)
fig, ax = canvas(84)
O = (34, 32); RR = 38; RU = 20
M = pt(*O, RR, 40); U = pt(*O, RU, 115)
line(ax, [(O[0] - 26, O[1]), (82, O[1])], 'fixe'); line(ax, [(O[0], O[1] - 3), (O[0], 76)], 'fixe')
arc(ax, *O, RU, 0, 180, 'autre', dash=True)
arc(ax, *O, RU, 0, 115, 'varie', head=True, lw=1.4)
arrow(ax, O, M, 'sujet', lw=1.4)
arc(ax, *O, 9, 0, 40, 'sujet', head=True)
line(ax, [M, (M[0], O[1])], 'resultat', dash=True); line(ax, [M, (O[0], M[1])], 'resultat', dash=True)
disc(ax, *U, 1.3, 'autre'); disc(ax, *M, 1.5, 'sujet')
text(ax, M[0] + 3, M[1] + 3, r'$M$', 'sujet', 'm')
text(ax, *pt(*O, 27, 49), r'$r$', 'sujet', 'm')
text(ax, 47.5, 35.5, r'$\theta$', 'sujet', 's')
text(ax, (M[0] + O[0]) / 2, O[1] - 3.5, r'$r\cos\theta$', 'resultat', 's')
text(ax, M[0] + 2, (M[1] + O[1]) / 2, r'$r\sin\theta$', 'resultat', 's', ha='left')
text(ax, U[0] - 2.5, U[1] + 1, r'$(\cos t,\sin t)$', 'autre', 's', ha='right')
text(ax, 32.5, 42.5, r'$t$ varie', 'varie', 's', ha='right')
for i, (role, s) in enumerate([('sujet', 'polaires : r et θ'), ('autre', 'paramétrique : t'), ('resultat', 'vecteur : r cos θ et r sin θ')]):
    yy = 20 - i * 7
    box(ax, 4, yy - 2, 3.5, 3.5, role); text(ax, 10, yy - 0.3, s, role, 'm', ha='left')
save(fig, '28-148')
