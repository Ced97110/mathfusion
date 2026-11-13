import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
s = 3.3
H0 = (14, 8); P = (H0[0] + 5.38 * s, 8); R = (H0[0], 8 + 12.92 * s)
poly(ax, [H0, P, R], 'sujet')
line(ax, [(H0[0] + 2, 8), (H0[0] + 2, 10), (H0[0], 10)], 'sujet', lw=0.6)
text(ax, H0[0] - 3, 5, 'H', 'sujet', 's'); text(ax, P[0] + 2, 5, 'P', 'sujet', 's'); text(ax, H0[0], R[1] + 3, 'R', 'sujet', 's')
text(ax, (H0[0] + P[0]) / 2, 4, 'HP = 5,38', 'fixe', 's')
text(ax, H0[0] - 1.5, 29, 'RH\n12,92', 'fixe', 's', ha='right')
mx, my = (P[0] + R[0]) / 2 + 4.0, (P[1] + R[1]) / 2 + 1.7
text(ax, mx, my, 'x + y = 14', 'sujet', 's', rot=-67)
y0 = 60
text(ax, 42, y0 + 11.5, 'Pythagore dans PHR', 'sujet', 's', ha='left')
box(ax, 42, y0 - 2, 44, 11, 'sujet', label=r'$(x+y)^2 = RH^2 + HP^2$', size='s')
text(ax, 42, y0 - 4.5, 'même carré, développé', 'varie', 's', ha='left')
box(ax, 42, y0 - 18, 44, 11, 'varie', label=r'$(x+y)^2 = x^2 + 2xy + y^2$', size='s')
box(ax, 42, y0 - 34, 44, 11, 'resultat', label='on égale les deux écritures :\n' + r'$x^2$ et $y^2$ s’annulent', size='s')
arrow(ax, (82, y0 - 2), (82, y0 - 7), 'fixe'); arrow(ax, (82, y0 - 18), (82, y0 - 23), 'fixe')
save(fig, '34-050')
