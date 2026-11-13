import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# v = <50, 86,60> ; 0,6 mm par unité sur les deux axes
ox, oy, s = 12, 14, 0.6
P = lambda x, y: (ox + x * s, oy + y * s)
arrow(ax, P(0, 0), P(50, 0), 'varie', lw=1.5)
arrow(ax, P(50, 0), P(50, 86.6), 'varie', lw=1.5)
arrow(ax, P(0, 0), P(50, 86.6), 'sujet', lw=1.6)
line(ax, [P(0, 0), P(0, 95)], 'fixe', lw=0.5)
text(ax, P(25, 0)[0], oy - 5, r'$50\,i$', 'varie', 's')
text(ax, P(50, 43)[0] + 11, P(50, 43)[1], r'$86{,}60\,j$', 'varie', 's')
text(ax, P(22, 50)[0] - 3, P(22, 50)[1] + 3, 'vent', 'sujet', 's')
box(ax, 50, 56, 36, 20, 'resultat')
text(ax, 68, 69, r'$a=50$', 'resultat', 's')
text(ax, 68, 62, r'$b=86{,}60$', 'resultat', 's')
text(ax, 68, 46, 'un seul choix', 'resultat', 's')
save(fig, '41-160')
