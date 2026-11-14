import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
ox, oy, u = 14, 24, 22
arrow(ax, (ox, oy), (ox + u, oy), 'sujet', lw=1.5)
arrow(ax, (ox, oy), (ox, oy + u), 'varie', lw=1.5)
arrow(ax, (ox, oy - 4), (ox + u, oy - 4), 'resultat', lw=1.5)
text(ax, ox + u / 2, oy + 3.5, r'$x = (1, 0)$', 'sujet', 's')
text(ax, ox + 3, oy + u + 4, r'$Tx = (0, 1)$', 'varie', 's', ha='left')
text(ax, ox + u / 2, oy - 8.5, r'$T^2x = (1, 0)$', 'resultat', 's')
tx = 50
text(ax, tx, 58, '3 vecteurs', 'encre', 's', ha='left', weight='bold')
text(ax, tx, 53, 'dans un plan :', 'encre', 's', ha='left', weight='bold')
text(ax, tx, 46, 'ils sont liés', 'limite', 's', ha='left')
text(ax, tx, 36, r'$T^2x - x = 0$', 'encre', 's', ha='left')
text(ax, tx, 28, r'$g = \lambda^2 - 1$', 'resultat', 's', ha='left', weight='bold')
text(ax, tx, 22, r'$g(\lambda)\,x = 0$', 'resultat', 's', ha='left')
save(fig, '60-149')
