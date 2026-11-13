import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
c = (12, 12); s = 11.0
def P(r, d): return (c[0] + s * r * math.cos(math.radians(d)), c[1] + s * r * math.sin(math.radians(d)))
def arc(r, d0, d1, n=40): return [P(r, d0 + (d1 - d0) * i / n) for i in range(n + 1)]
# axes
arrow(ax, (c[0] - 3, c[1]), (c[0] + 40, c[1]), 'fixe', lw=0.7)
arrow(ax, (c[0], c[1] - 3), (c[0], c[1] + 54), 'fixe', lw=0.7)
# rays: z (4, 90°), w (2, 30°), q (2, 60°)
arrow(ax, c, P(4, 90), 'sujet', lw=1.2)
arrow(ax, c, P(2, 30), 'autre', lw=1.2)
arrow(ax, c, P(2, 60), 'resultat', lw=1.4)
line(ax, arc(1.1, 0, 30), 'autre'); line(ax, arc(1.7, 0, 60), 'resultat')
text(ax, c[0] + 4, c[1] + 54, 'z = 4 cis 90°', 'sujet', 's', ha='left')
text(ax, P(2, 30)[0] + 2, P(2, 30)[1] - 3.5, 'w = 2 cis 30°', 'autre', 's', ha='left')
text(ax, P(2, 60)[0] + 2.5, P(2, 60)[1] + 4, 'q = 2 cis 60°', 'resultat', 's', ha='left')
# right column: the two actions
box(ax, 50, 52, 36, 9, 'fixe', label='modules : 4 ÷ 2 = 2', size='s')
box(ax, 50, 40, 36, 9, 'fixe', label='angles : 90° − 30° = 60°', size='s')
arrow(ax, (68, 40), (68, 30), 'varie')
box(ax, 50, 18, 36, 11, 'resultat', label='q = 2 cis 60°', size='s')
text(ax, 68, 11, 'q × w : 2 × 2 = 4 et', 'encre', 's')
text(ax, 68, 6.5, '60° + 30° = 90°', 'encre', 's')
save(fig, '39-073')
