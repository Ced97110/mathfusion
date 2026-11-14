import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 52, r'facteur commun $y^2+1$', 'sujet', 'm', weight='bold')
# gauche : courbe y^2 + 1 sans racine réelle
ox, oy = 20, 16
arrow(ax, (4, oy), (36, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 2), (ox, 42), 'fixe', lw=0.7)
pts = [(ox + t * 7, oy + (t * t + 1) * 4.5) for t in [i / 10 for i in range(-20, 21)]]
line(ax, pts, 'sujet', lw=1.3)
text(ax, 31, 44, r'$y^2+1$', 'sujet', 's')
text(ax, ox, 9, 'aucune racine réelle', 'fixe', 's')
# droite : plan des nombres complexes
cx, cy = 66, 28
arrow(ax, (50, cy), (84, cy), 'fixe', lw=0.7)
arrow(ax, (cx, 10), (cx, 44), 'fixe', lw=0.7)
disc(ax, cx, cy + 8, 1.8, 'resultat')
disc(ax, cx, cy - 8, 1.8, 'resultat')
text(ax, cx + 4, cy + 8, r'$i$', 'resultat', 'm')
text(ax, cx + 5, cy - 8, r'$-i$', 'resultat', 'm')
text(ax, 82, cy + 4, r'$\mathbb{C}$', 'fixe', 'm')
text(ax, cx, 5, r'$i^2=-1$ : racines dans $\mathbb{C}$', 'resultat', 's')
save(fig, '70-044')
