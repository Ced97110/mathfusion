import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

fig, ax = canvas(46)
O = (12, 10); P = pt(O, 32, 30); H = (P[0], O[1])      # 40 km -> 32 mm
arrow(ax, O, (58, 10), 'fixe', lw=0.9)
line(ax, [O, H], 'fixe', lw=1.0, dash=True)
line(ax, [H, P], 'fixe', lw=1.0, dash=True)
line(ax, [O, P], 'sujet', lw=2.2)
disc(ax, O[0], O[1], 1.5, 'sujet'); disc(ax, P[0], P[1], 1.5, 'sujet')
text(ax, 9.3, 13.5, 'O'); text(ax, P[0] + 2.5, P[1] + 2.5, 'P')
text(ax, 20, 30, 'r = OP = 40 km', 'sujet', 'm')
text(ax, 60, 20, 'en ligne droite', 'fixe', 's')
arrow(ax, (52, 20), (44, 25), 'fixe', lw=0.6)
save(fig, '39-015')
