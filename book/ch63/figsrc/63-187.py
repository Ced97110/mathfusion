import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# plan des couples (x1, x2) ; échange = miroir sur la diagonale
ox, oy, L = 14, 14, 44
arrow(ax, (ox, oy), (ox + L + 4, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy), (ox, oy + L + 4), 'fixe', lw=0.7)
line(ax, [(ox, oy), (ox + L, oy + L)], 'resultat', dash=True)
text(ax, ox + L - 2, oy + L + 3, 'x₁ = x₂'.replace('x₁ = x₂', r'$x_1 = x_2$'), 'resultat', 's', ha='right')
a, b = 14, 34
P, Q = (ox + a, oy + b), (ox + b, oy + a)
for p in (P, Q):
    line(ax, [(ox, p[1]), p], 'fixe', lw=0.5, dash=True)
    line(ax, [(p[0], oy), p], 'fixe', lw=0.5, dash=True)
disc(ax, P[0], P[1], 1.8, 'sujet'); disc(ax, Q[0], Q[1], 1.8, 'varie')
arrow(ax, (P[0] + 3, P[1] - 1.2), (Q[0] - 3, Q[1] + 1.2), 'varie', curve=-0.3)
text(ax, P[0] - 2, P[1] + 5, r'$(x_1, x_2)$', 'sujet', 's', ha='left')
text(ax, Q[0] + 2.5, Q[1] - 4, r'$(x_2, x_1)$', 'varie', 's', ha='left')
text(ax, ox + a, oy - 3.5, r'$x_1$', 'fixe', 's'); text(ax, ox + b, oy - 3.5, r'$x_2$', 'fixe', 's')
text(ax, ox - 3.5, oy + a, r'$x_1$', 'fixe', 's'); text(ax, ox - 3.5, oy + b, r'$x_2$', 'fixe', 's')
x0 = 62
text(ax, x0, 70, r'$S_2$ échange', 'varie', 's')
text(ax, x0, 64, r'$x_1$ et $x_2$', 'varie', 's')
text(ax, x0, 50, r'$x_1 + x_2$', 'resultat', 'm'); text(ax, x0, 44, 'inchangé', 'resultat', 's')
text(ax, x0, 33, r'$x_1 x_2$', 'resultat', 'm'); text(ax, x0, 27, 'inchangé', 'resultat', 's')
text(ax, x0 + 3, 4, r'$\mathrm{Inv}\,S_2 = F(p_1, p_2)$', 'sujet', 's')
save(fig, '63-187')
