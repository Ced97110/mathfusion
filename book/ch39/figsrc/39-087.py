import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 11.0
def plane(c):
    arrow(ax, (c[0] - 11, c[1]), (c[0] + 30, c[1]), 'fixe', lw=0.6)
    arrow(ax, (c[0], c[1] - 11), (c[0], c[1] + 30), 'fixe', lw=0.6)
def P(c, r, d): return (c[0] + s * r * math.cos(math.radians(d)), c[1] + s * r * math.sin(math.radians(d)))
# left : 2 cis 30° and 2 cis 390° = same point
c1 = (14, 22); plane(c1)
sp = [P(c1, 0.45 + 0.0012 * d, d) for d in range(0, 391, 6)]
line(ax, sp, 'varie', lw=1.3)
arrow(ax, sp[-2], sp[-1], 'varie', lw=1.3)
arrow(ax, c1, P(c1, 2, 30), 'resultat', lw=1.2)
disc(ax, *P(c1, 2, 30), 1.6, 'resultat')
text(ax, 22, 54, '+ 360° : un tour', 'varie', 's')
text(ax, 22, 6, '30° et 390° : même point', 'resultat', 's')
# right : 2 cis 30° and 2 cis 40° = two points
c2 = (58, 22); plane(c2)
arrow(ax, c2, P(c2, 2, 30), 'sujet', lw=1.2)
arrow(ax, c2, P(c2, 2, 40), 'autre', lw=1.2)
disc(ax, *P(c2, 2, 30), 1.4, 'sujet'); disc(ax, *P(c2, 2, 40), 1.4, 'autre')
line(ax, [P(c2, 1.2, 30 + 10 * i / 10) for i in range(11)], 'varie', lw=1.2)
text(ax, 72, 40, '10°', 'varie', 's')
text(ax, 66, 6, '30° et 40° : deux points', 'autre', 's')
text(ax, 22, 48, '2 cis 30° = 2 cis 390°', 'encre', 's')
text(ax, 66, 48, '2 cis 30° ≠ 2 cis 40°', 'encre', 's')
save(fig, '39-087')
