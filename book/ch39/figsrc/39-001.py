import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

def arc(ax, o, r, d0, d1, role='encre'):
    line(ax, [pt(o, r, d0 + (d1 - d0) * i / 40) for i in range(41)], role)

fig, ax = canvas(50)
O = (12, 14); s = 0.8                      # 40 km -> 32 mm
P = pt(O, 40 * s, 30); H = (P[0], O[1])
arrow(ax, O, (58, 14), 'fixe', lw=0.9)
line(ax, [O, H], 'varie', lw=1.8)
line(ax, [H, P], 'resultat', lw=1.8)
line(ax, [O, P], 'sujet', lw=1.8)
arc(ax, O, 9, 0, 30)
disc(ax, O[0], O[1], 1.3, 'sujet'); disc(ax, P[0], P[1], 1.3, 'sujet')
text(ax, 9.3, 11, 'O'); text(ax, P[0] + 2.5, P[1] + 2.5, 'P')
text(ax, 24.0, 26.0, '40 km', 'sujet')
text(ax, 25.9, 10.3, r'$x=\ ?$', 'varie')
text(ax, H[0] + 6, 22, r'$y=\ ?$', 'resultat')
text(ax, 25.0, 17.6, '30°')
text(ax, 55, 10.5, 'est', 'fixe')
box(ax, 62, 33, 24, 14, 'sujet', label='Radar :\n40 km, 30°')
box(ax, 62, 11, 24, 14, 'varie', label='Pilote veut :\nx et y')
save(fig, '39-001')
