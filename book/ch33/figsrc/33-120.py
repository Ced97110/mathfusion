import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
O = (30, 34); R = 24; t = -math.atan(3/4)
cp = [(O[0]+R*math.cos(a), O[1]+R*math.sin(a)) for a in [i*2*math.pi/120 for i in range(121)]]
poly(ax, cp, 'fixe'); line(ax, cp, 'fixe')
line(ax, [(O[0]-R-4, O[1]), (O[0]+R+4, O[1])], 'fixe'); line(ax, [(O[0], O[1]-R-4), (O[0], O[1]+R+4)], 'fixe')
P = (O[0]+R*math.cos(t), O[1]+R*math.sin(t))
line(ax, [O, P], 'sujet', lw=1.6)
line(ax, [P, (P[0], O[1])], 'varie', dash=True)
line(ax, [O, (P[0], O[1])], 'resultat', lw=2.4)
disc(ax, P[0], P[1], 1.4, 'sujet')
line(ax, [(O[0]+8*math.cos(a), O[1]+8*math.sin(a)) for a in [i*t/20 for i in range(21)]], 'varie', lw=1.0)
text(ax, O[0]+12, O[1]-3.5, r'$\theta<0$', 'varie', 's')
text(ax, (O[0]+P[0])/2, O[1]+3, r'$\cos\theta=\frac{4}{5}$', 'resultat', 's')
text(ax, P[0]+2, (O[1]+P[1])/2, r'$-\frac{3}{5}$', 'varie', 's', ha='left')
text(ax, 72, 56, r'pente $-\frac{3}{4}$', 'sujet', 's')
text(ax, 72, 14, 'point à droite :', 'resultat', 's'); text(ax, 72, 10, 'abscisse > 0', 'resultat', 's')
save(fig, '33-120')
