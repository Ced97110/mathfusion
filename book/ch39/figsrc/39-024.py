import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

fig, ax = canvas(46)
O = (12, 20); P = pt(O, 32, 30); H = (P[0], O[1])      # 40 km -> 32 mm
arrow(ax, O, (58, 20), 'fixe', lw=0.9)
line(ax, [O, P], 'fixe', lw=1.0)
line(ax, [H, P], 'fixe', lw=1.0, dash=True)
line(ax, [O, H], 'varie', lw=2.2)
line(ax, [(H[0] - 2.2, H[1]), (H[0] - 2.2, H[1] + 2.2), (H[0], H[1] + 2.2)], 'encre', lw=0.7)
disc(ax, O[0], O[1], 1.3, 'fixe'); disc(ax, P[0], P[1], 1.3, 'fixe'); disc(ax, H[0], H[1], 1.3, 'varie')
text(ax, 9.3, 23.5, 'O'); text(ax, P[0] + 2.5, P[1] + 2.5, 'P'); text(ax, H[0] + 3, 17, 'H')
text(ax, 22.5, 33, '40 km, 30°', 'fixe', 's')
brace(ax, O[0], H[0], 17, 'varie', label='x = OH ≈ 34,64 km', down=True)
text(ax, 49, 25, 'lu sur l’axe horizontal', 'fixe', 's', ha='left')
save(fig, '39-024')
