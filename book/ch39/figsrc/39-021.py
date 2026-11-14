import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

def arc(ax, o, r, d0, d1, role='encre', dash=False):
    line(ax, [pt(o, r, d0 + (d1 - d0) * i / 60) for i in range(61)], role, dash=dash)

fig, ax = canvas(54)
O = (14, 12); P = pt(O, 32, 50)
for r in (12, 22, 32):
    arc(ax, O, r, 0, 90, 'fixe', dash=True)
arrow(ax, O, (68, 12), 'fixe', lw=0.9)
line(ax, [O, P], 'sujet', lw=1.8)
arc(ax, O, 7, 0, 50, 'encre')
disc(ax, P[0], P[1], 1.4, 'sujet'); disc(ax, O[0], O[1], 2.2, 'sujet')
text(ax, 18, 5.5, 'O : origine, pôle', 'sujet', 'm')
text(ax, P[0] + 3, P[1] + 2.5, 'P'); text(ax, 21.3, 28, 'OP', 'sujet')
text(ax, 74, 12, 'Ox', 'fixe', 'm')
text(ax, 54, 47, 'distances comptées depuis O', 'fixe', 's')
save(fig, '39-021')
