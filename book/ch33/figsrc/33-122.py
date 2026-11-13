import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
O = (30, 20); R = 18
cp = [(O[0]+R*math.cos(a), O[1]+R*math.sin(a)) for a in [i*2*math.pi/120 for i in range(121)]]
poly(ax, cp, 'sujet'); line(ax, cp, 'sujet')
line(ax, [(O[0]-R-3, O[1]), (O[0]+R+3, O[1])], 'fixe')
line(ax, [O, (O[0], O[1]+2*R+6)], 'fixe')
for k, lab in ((0, '0'), (1, '1'), (2, '2')):
    ax.plot([O[0]-1.2, O[0]+1.2], [O[1]+k*R]*2, color=COL['fixe'], lw=0.8, zorder=3)
    text(ax, O[0]-3.2, O[1]+k*R+1.8, lab, 'fixe', 's')
line(ax, [(O[0]-R-3, O[1]+2*R), (O[0]+R+3, O[1]+2*R)], 'limite', dash=True)
disc(ax, O[0], O[1]+R, 1.4, 'resultat')
text(ax, O[0]+8, O[1]+R+4, 'hauteur 1 : le plus haut', 'resultat', 's', ha='left')
text(ax, O[0]+R+5, O[1]+2*R-4, 'hauteur 2 :', 'limite', 's', ha='left'); text(ax, O[0]+R+5, O[1]+2*R-8, 'aucun point', 'limite', 's', ha='left')
text(ax, O[0]+6, O[1]-6, 'rayon 1', 'sujet', 's')
save(fig, '33-122')
