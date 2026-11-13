import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

fig, ax = canvas(46)
O = (12, 10); P = pt(O, 32, 30); H = (P[0], O[1])      # 40 km -> 32 mm
arrow(ax, O, (58, 10), 'fixe', lw=0.9)
line(ax, [O, P], 'fixe', lw=1.0)
line(ax, [O, H], 'fixe', lw=1.0)
line(ax, [H, P], 'resultat', lw=2.2)
disc(ax, O[0], O[1], 1.3, 'fixe'); disc(ax, P[0], P[1], 1.3, 'resultat'); disc(ax, H[0], H[1], 1.3, 'fixe')
text(ax, 9.3, 13.5, 'O'); text(ax, P[0] - 0.5, P[1] + 3.5, 'P'); text(ax, H[0], 6.6, 'H')
text(ax, 22, 22, '40 km, 30°', 'fixe', 's')
arrow(ax, (H[0] + 3, 10.5), (H[0] + 3, P[1] - 0.5), 'resultat', both=True, lw=0.8)
text(ax, H[0] + 5.5, 24, 'y = HP', 'resultat', 'l', ha='left', weight='bold')
text(ax, H[0] + 5.5, 18.5, 'vers le nord', 'resultat', 's', ha='left')
line(ax, [(H[0] - 2.2, 10), (H[0] - 2.2, 12.2), (H[0], 12.2)], 'fixe', lw=0.8)
text(ax, 22, 4.5, 'axe horizontal', 'fixe', 's')
save(fig, '39-014')
