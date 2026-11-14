import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))

fig, ax = canvas(68)
o = (44, 12); u = 10
X = iso(1, 0, 1, o, u); U = iso(0, 1, 0, o, u); R = iso(2, 1, 2, o, u); D = iso(2, 0, 2, (0, 0), u)
arrow(ax, o, X, 'sujet', lw=1.3)
arrow(ax, o, U, 'varie', lw=1.3)
arrow(ax, U, R, 'sujet', lw=1.0)
line(ax, [o, U], 'varie', lw=0.0)
dot(ax, R, 'resultat', 1.8)
text(ax, X[0] + 3, X[1] + 1, 'x = (1, 0, 1)', 'sujet', 's', ha='left')
text(ax, U[0] - 3, U[1] - 4, 'u = (0, 1, 0)', 'varie', 's', ha='right')
text(ax, R[0] + 3, R[1] + 3, 'ρ(u) = (2, 1, 2)', 'resultat', 's', ha='left')
text(ax, (U[0] + R[0]) / 2 - 3, (U[1] + R[1]) / 2 + 2, '+ 2x', 'sujet', 's', ha='right')
text(ax, o[0], 4, 'x ne bouge pas ; Q = 1 avant et après', 'encre', 's')
save(fig, '73-204')
