import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
o = (8, 8); u = 2.5
P = lambda k: (o[0] + u*k, o[1] + u*k)
line(ax, [o, P(17)], 'sujet', lw=1.2)
for k in (1, 2, 5): disc(ax, *P(k), 1.0, 'sujet')
for k in (3, 6, 15): disc(ax, *P(k), 1.0, 'resultat')
disc(ax, *o, 1.0, 'fixe')
for a, b in ((1, 3), (2, 6), (5, 15)):
    arrow(ax, (P(a)[0]+1.5, P(a)[1]-1.5), (P(b)[0]+1.5, P(b)[1]-1.5), 'varie', curve=-0.25)
text(ax, 22, 6, 'origine : ne bouge pas', 'fixe', 's', ha='left')
text(ax, 60, 52, 'points de départ', 'sujet', 's'); text(ax, 60, 46, 'images par ×3', 'resultat', 's')
text(ax, 60, 40, 'même droite', 'encre', 's')
save(fig, '73-055')
