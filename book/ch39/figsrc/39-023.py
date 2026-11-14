import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

def arc(ax, o, r, d0, d1, role='encre'):
    line(ax, [pt(o, r, d0 + (d1 - d0) * i / 40) for i in range(41)], role)

fig, ax = canvas(50)
O = (12, 14); P = pt(O, 40, 30)
arrow(ax, O, (58, 14), 'fixe', lw=1.4)
line(ax, [O, P], 'sujet', lw=1.8)
arc(ax, O, 14, 0, 30, 'varie')
arrow(ax, pt(O, 14, 26), pt(O, 14, 31), 'varie', lw=1.0)
disc(ax, O[0], O[1], 1.3, 'fixe'); disc(ax, P[0], P[1], 1.3, 'sujet')
text(ax, 9.3, 11, 'O')
text(ax, 36, 9.5, 'Ox : côté de départ', 'fixe', 's')
text(ax, P[0] + 2, P[1] + 3.5, "OP : côté d'arrivée", 'sujet', 's', ha='left')
text(ax, 32, 19.5, r'$\theta=30°$', 'varie', 'l')
text(ax, 44, 46, 'θ : de Ox vers OP', 'encre', 'm')
save(fig, '39-023')
