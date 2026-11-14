import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))
def arc(ax, c, r, a0, a1, role, lw=1.1, head=True):
    pts = [P(c, r, a0 + (a1 - a0) * i / 40) for i in range(41)]
    line(ax, pts, role, lw)
    if head: arrow(ax, pts[-4], pts[-1], role, lw)

fig, ax = canvas(92)
c = (44, 62); r = 20
disc(ax, *c, r, 'autre')
for a in (0, 30, 60, 90):
    line(ax, [c, P(c, r, a)], 'fixe', lw=0.6, dash=True)
    dot(ax, P(c, r, a), 'sujet' if a else 'autre', 1.7)
text(ax, c[0] + r + 5, c[1], '1', 'autre', 's')
text(ax, *P(c, r + 6, 30), '30°', 'autre', 's')
text(ax, *P(c, r + 6, 60), '60°', 'autre', 's')
text(ax, c[0], c[1] + r + 5, '90°', 'autre', 's')
text(ax, c[0] - 8, c[1] - 8, 'cercle', 'autre', 's')
box(ax, 14, 24, 60, 10, 'autre', label='30° + 60° = 90°')
box(ax, 4, 2, 80, 10, 'sujet', label='R(30°) R(60°) = R(90°)', size='m')
arrow(ax, (44, 22.5), (44, 13.5), 'fixe', both=True)
text(ax, 64, 18, 'même calcul', 'fixe', 's')
save(fig, '73-193')
