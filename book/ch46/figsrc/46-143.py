import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, r = 28, 30, 22
disc(ax, cx, cy, r, 'sujet')
def P(d): return (cx + r * math.cos(math.radians(d)), cy + r * math.sin(math.radians(d)))
for d, role, lab, dx, dy, ha in [(90, 'sujet', r'$z$ (90°)', 0, 3.0, 'center'), (30, 'autre', r'$w$ (30°)', 2, 0, 'left'),
                                 (-30, 'autre', r'$w^{-1}$ (−30°)', 2, 0, 'left'), (60, 'resultat', r'$zw^{-1}$ (60°)', 2, 3.2, 'left')]:
    x, y = P(d); line(ax, [(cx, cy), (x, y)], role, lw=0.6)
    disc(ax, x, y, 1.1, role); text(ax, x + dx, y + dy, lab, role, 's', ha=ha)
text(ax, 28, 3, 'tous de module 1 : dans $\\mathbb{T}$', 'resultat', 's')
save(fig, '46-143')
