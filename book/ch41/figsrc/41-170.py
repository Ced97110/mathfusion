import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
# gauche : dans l'espace, i et j, une seule droite perpendiculaire aux deux
o, u = (24, 26), 14.0
I = lambda x, y, z: iso(x, y, z, o, u)
poly(ax, [I(0, 0, 0), I(1, 0, 0), I(1, 1, 0), I(0, 1, 0)], 'fixe')
line(ax, [I(0, 0, -1.2), I(0, 0, 2.2)], 'resultat', lw=0.8, dash=True)
arrow(ax, I(0, 0, 0), I(1, 0, 0), 'sujet', lw=1.5)
arrow(ax, I(0, 0, 0), I(0, 1, 0), 'autre', lw=1.5)
arrow(ax, I(0, 0, 0), I(0, 0, 1), 'resultat', lw=1.6)
text(ax, I(1, 0, 0)[0] + 3, I(1, 0, 0)[1] - 1, r'$i$', 'sujet', 's')
text(ax, I(0, 1, 0)[0] - 3, I(0, 1, 0)[1] - 1, r'$j$', 'autre', 's')
text(ax, I(0, 0, 1)[0] + 7, I(0, 0, 1)[1] + 2, r'$k=i\times j$', 'resultat', 's')
text(ax, 22, 70, 'espace : une droite', 'resultat', 's')
# droite : dans le plan, une seule direction perpendiculaire à <3, 4>
ox, oy, s = 66, 36, 4.5
P = lambda x, y: (ox + x * s, oy + y * s)
line(ax, [P(4, -3), P(-4, 3)], 'resultat', lw=0.8, dash=True)
arrow(ax, P(0, 0), P(3, 4), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(-4, 3), 'resultat', lw=1.6)
text(ax, P(3, 4)[0] + 2, P(3, 4)[1] + 4, r'$\langle 3,\ 4\rangle$', 'sujet', 's')
text(ax, P(-4, 3)[0] - 1, P(-4, 3)[1] + 4, r'$\langle -4,\ 3\rangle$', 'resultat', 's')
d1, d2 = (0.6, 0.8), (-0.8, 0.6)
line(ax, [(ox + 3.5 * d1[0], oy + 3.5 * d1[1]), (ox + 3.5 * (d1[0] + d2[0]), oy + 3.5 * (d1[1] + d2[1])), (ox + 3.5 * d2[0], oy + 3.5 * d2[1])], 'fixe', lw=0.6)
text(ax, 66, 70, 'plan : une droite', 'resultat', 's')
save(fig, '41-170')
