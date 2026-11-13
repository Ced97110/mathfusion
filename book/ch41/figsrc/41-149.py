import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
ox, oy, s = 14, 14, 10.0
P = lambda x, y: (ox + x * s, oy + y * s)
arrow(ax, P(-0.8, 0), P(6.5, 0), 'fixe', lw=0.7)
arrow(ax, P(0, -0.8), P(0, 4.5), 'fixe', lw=0.7)
arrow(ax, P(0, 0), P(4, 0), 'autre', lw=1.4)
arrow(ax, P(0, 0), P(0, 3), 'sujet', lw=1.4)
line(ax, [(ox + 3, oy), (ox + 3, oy + 3), (ox, oy + 3)], 'fixe', lw=0.6)  # repère de l'angle droit
disc(ax, ox, oy, 1.4, 'resultat')
text(ax, ox - 1, oy + 33, r'$u=\langle 0,\ 3\rangle$', 'sujet', 's', ha='left')
text(ax, ox + 46, oy + 5, r'$v=\langle 4,\ 0\rangle$', 'autre', 's')
text(ax, ox + 3.2, oy - 5.5, r'$H=O$', 'resultat', 's')
text(ax, 68, 62, r'$0\times 4+3\times 0=0$', 'encre', 's')
box(ax, 44, 36, 40, 14, 'resultat', label='projection = vecteur nul', size='s')
save(fig, '41-149')
