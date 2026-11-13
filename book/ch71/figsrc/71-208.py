import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
o = (14, 14); s = 9
G = lambda x, y: (o[0] + x * s, o[1] + y * s)
arrow(ax, G(-1, 0), G(8.5, 0), 'fixe', lw=0.6); arrow(ax, G(0, -1), G(0, 5.5), 'fixe', lw=0.6)
line(ax, [G(-1.5, 3), G(4.5, -1)], 'sujet', lw=1.4)
line(ax, [G(-0.6, 2.4), G(5.7, -1.8)], 'sujet', lw=1.4) if False else None
line(ax, [G(-3, 2), G(3, -2)], 'fixe', lw=0.9, dash=True) if False else None
disc(ax, *G(3, 0), 1.0, 'sujet'); disc(ax, *G(0, 2), 1.0, 'sujet')
arrow(ax, G(3, 0), G(5, 3), 'varie', lw=1.4)
text(ax, G(3, 0)[0] + 1, G(3, 0)[1] - 3.5, r'$(3,0)$', 'sujet', 's', ha='left'); text(ax, G(0, 2)[0] + 2, G(0, 2)[1] + 3, r'$(0,2)$', 'sujet', 's', ha='left')
text(ax, G(5, 3)[0], G(5, 3)[1] + 3, r'$(2,3)$', 'varie', 's')
text(ax, 44, 67, r'droite $2x+3y=6$ : niveau $6$', 'sujet', 's')
text(ax, 44, 61, r'direction $(3,-2)$', 'sujet', 's')
text(ax, 62, 4, r'$2\times3+3\times(-2)=0$', 'resultat', 's')
save(fig, '71-208')
