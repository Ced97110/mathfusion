import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(64)
O = (44, 14); R = 28
cp = [(O[0]+R*math.cos(a), O[1]+R*math.sin(a)) for a in [i*math.pi/80 for i in range(81)]]
poly(ax, cp, 'sujet'); line(ax, cp, 'sujet')
line(ax, [(O[0]-R-4, O[1]), (O[0]+R+4, O[1])], 'fixe')
line(ax, [(O[0]-R-4, O[1]+R), (O[0]+R+4, O[1]+R)], 'resultat', dash=True)
for d in (20, 50, 90, 130, 160):
    a = math.radians(d); P = (O[0]+R*math.cos(a), O[1]+R*math.sin(a))
    line(ax, [(P[0], O[1]), P], 'varie', lw=1.6)
    disc(ax, P[0], P[1], 1.2, 'sujet')
text(ax, O[0]-R+9, O[1]+R+3.5, 'hauteur 1 : le maximum', 'resultat', 's')
text(ax, 80, O[1]+9, 'sinus =', 'varie', 's'); text(ax, 80, O[1]+5, 'hauteur', 'varie', 's')
text(ax, O[0], O[1]-3.5, 'cercle de rayon 1', 'sujet', 's')
save(fig, '33-123')
