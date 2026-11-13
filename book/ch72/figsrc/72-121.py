import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, u = 30, 38, 16
arrow(ax, (6, oy), (56, oy), 'fixe', lw=0.8); arrow(ax, (ox, 12), (ox, 66), 'fixe', lw=0.8)
line(ax, [(ox - 20, oy - 20), (ox + 20, oy + 20)], 'limite', lw=1.0, dash=True)
arrow(ax, (ox, oy), (ox + u, oy + u), 'limite', lw=1.6)
arrow(ax, (ox, oy), (ox + u / 2, oy - u / 2), 'varie', lw=1.6)
text(ax, ox + u + 3, oy + u + 3, r'$z$', 'limite', 'm'); text(ax, ox + u / 2 + 1, oy - u / 2 - 4, r'$w$', 'varie', 'm')
text(ax, 72, 56, 'droite de $z$ :', 'limite', 's'); text(ax, 72, 52, 'dégénérée', 'limite', 's')
text(ax, 72, 36, r'$B(z,w)=1$', 'encre', 's')
text(ax, 72, 22, r'$z$ et $w$ :', 'resultat', 's'); text(ax, 72, 18, 'plan non dégénéré', 'resultat', 's')
save(fig, '72-121')
