import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
c = (12, 30); s = 6.5
def P(r, d): return (c[0] + s * r * math.cos(math.radians(d)), c[1] + s * r * math.sin(math.radians(d)))
def arc(r, d0, d1, n=40): return [P(r, d0 + (d1 - d0) * i / n) for i in range(n + 1)]
arrow(ax, (c[0] - 3, c[1]), (c[0] + 66, c[1]), 'fixe', lw=0.7)
arrow(ax, (c[0], c[1] - 3), (c[0], c[1] + 61), 'fixe', lw=0.7)
arrow(ax, c, P(2, 30), 'sujet', lw=1.3)
arrow(ax, c, P(4, 60), 'varie', lw=1.3)
arrow(ax, c, P(8, 90), 'resultat', lw=1.5)
line(ax, arc(1.2, 0, 30), 'sujet'); line(ax, arc(2.4, 0, 60), 'varie')
text(ax, P(2, 30)[0] + 2, P(2, 30)[1] - 3, 'z : 2 cis 30°', 'sujet', 's', ha='left')
text(ax, P(4, 60)[0] + 2.5, P(4, 60)[1] + 1, '$z^{2}$ : 4 cis 60°', 'varie', 's', ha='left')
text(ax, c[0] + 3, c[1] + 61, '$z^{3}$ : 8 cis 90°', 'resultat', 's', ha='left')
box(ax, 4, 11, 80, 8, 'fixe', label='modules : 2 × 2 × 2 = 8', size='s')
box(ax, 4, 1.5, 80, 8, 'fixe', label='angles : 30° + 30° + 30° = 90°', size='s')
save(fig, '39-075')
