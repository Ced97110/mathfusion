import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))
def arc(ax, c, r, a0, a1, role, lw=1.1, head=True):
    pts = [P(c, r, a0 + (a1 - a0) * i / 40) for i in range(41)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-4], pts[-1], role, lw)

fig, ax = canvas(72)
c = (12, 10)
line(ax, [c, P(c, 52, 0)], 'fixe', lw=1.0)
line(ax, [c, P(c, 52, 30)], 'varie', lw=1.0)
line(ax, [c, P(c, 52, 90)], 'resultat', lw=1.4)
arc(ax, c, 17, 0, 30, 'varie')
arc(ax, c, 25, 30, 90, 'autre')
line(ax, [(c[0] + 6, c[1]), (c[0] + 6, c[1] + 6), (c[0], c[1] + 6)], 'resultat', lw=0.8)
text(ax, *P(c, 22, 14), '30°', 'varie', 's')
text(ax, *P(c, 33, 62), '60°', 'autre', 's')
text(ax, 16, 67, '90° : quart de tour', 'resultat', 's', ha='left')
text(ax, 34, 58, 'R(30°) R(60°) = R(90°)', 'sujet', 's', ha='left')
text(ax, 34, 50, 'R(60°) R(30°) = R(90°)', 'sujet', 's', ha='left')
text(ax, 34, 43, 'aussi 90° : ordre sans effet', 'fixe', 's', ha='left')
save(fig, '73-195')
