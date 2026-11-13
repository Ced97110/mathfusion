import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
o = (22, 28); s = 16
G = lambda x, y: (o[0] + x * s, o[1] + y * s)
arrow(ax, G(-1, 0), G(2.2, 0), 'fixe', lw=0.7); arrow(ax, G(0, -1.3), G(0, 1.7), 'fixe', lw=0.7)
line(ax, [G(-1, -1), G(1.7, 1.7)], 'resultat', dash=True)
arrow(ax, G(0, 0), G(1, 1), 'sujet', lw=1.4)
arrow(ax, G(0, 0), G(1, 0), 'autre', lw=1.4)
text(ax, G(1, 1)[0] - 3, G(1, 1)[1] + 2.5, r'$u=(1,1)$', 'sujet', 'm')
text(ax, G(1, 0)[0] + 1, G(1, 0)[1] - 3, r'$v=(1,0)$', 'autre', 'm')
text(ax, G(-0.9, -0.9)[0] + 12, G(-0.9, -0.9)[1] - 3.5, r'droite $Q=0$', 'resultat', 's')
box(ax, 50, 40, 36, 16, 'resultat'); text(ax, 68, 51.5, r'$Q(u)=1^2-1^2=0$', 'resultat', 's'); text(ax, 68, 44.5, r'$u\neq 0$ : isotrope', 'resultat', 's')
box(ax, 50, 12, 36, 16, 'limite'); text(ax, 68, 23.5, r'$B(u,v)=1\neq 0$', 'limite', 's'); text(ax, 68, 16.5, 'pas dans le radical', 'limite', 's')
save(fig, '71-193')
