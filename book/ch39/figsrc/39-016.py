import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

def arc(ax, o, r, d0, d1, role='encre'):
    line(ax, [pt(o, r, d0 + (d1 - d0) * i / 40) for i in range(41)], role)

fig, ax = canvas(48)
O = (12, 14); P = pt(O, 36, 30)
arrow(ax, O, (62, 14), 'fixe', lw=0.9)
line(ax, [O, P], 'fixe', lw=1.2)
arc(ax, O, 14, 0, 30, 'encre')
arrow(ax, pt(O, 14, 26), pt(O, 14, 31), 'encre', lw=0.9)
disc(ax, O[0], O[1], 1.3, 'fixe'); disc(ax, P[0], P[1], 1.3, 'fixe')
text(ax, 9.3, 11, 'O'); text(ax, P[0] + 2.5, P[1] + 2.5, 'P')
text(ax, 35, 19.5, r'$\theta=30°$', 'encre', 'l')
text(ax, 44, 9.5, 'axe horizontal (est)', 'fixe', 's')
text(ax, 44, 44, "θ se compte de l'est vers le nord", 'encre', 's')
save(fig, '39-016')
