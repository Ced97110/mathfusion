import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

def arc(ax, o, r, d0, d1, role='encre'):
    line(ax, [pt(o, r, d0 + (d1 - d0) * i / 40) for i in range(41)], role)

fig, ax = canvas(62)
line(ax, [(44, 4), (44, 52)], 'fixe', lw=0.6, dash=True)
for ox, title, sub in ((6, 'additionner', 'deux distances'), (50, 'multiplier', 'une distance, une direction')):
    O = (ox, 10); P = pt(O, 30, 40); H = (P[0], O[1])
    text(ax, ox + 19, 57, title, 'encre', 'm', weight='bold')
    text(ax, ox + 19, 52.5, sub, 'fixe', 's')
    arrow(ax, O, (ox + 34, 10), 'fixe', lw=0.9)
    disc(ax, O[0], O[1], 1.2, 'sujet'); disc(ax, P[0], P[1], 1.2, 'sujet')
    text(ax, ox - 0.5, 6.5, 'O'); text(ax, P[0] + 2.5, P[1] + 2.5, 'P')
    if ox == 6:
        line(ax, [O, H], 'varie', lw=1.8)
        line(ax, [H, P], 'resultat', lw=1.8)
        text(ax, (O[0] + H[0]) / 2, 6.5, 'x', 'varie')
        text(ax, H[0] + 2.5, (H[1] + P[1]) / 2, 'y', 'resultat')
    else:
        line(ax, [O, P], 'sujet', lw=1.8)
        arc(ax, O, 9, 0, 40)
        text(ax, O[0] + 12.5, 13.5, 'θ')
        text(ax, (O[0] + P[0]) / 2 - 2.5, (O[1] + P[1]) / 2 + 2.5, 'r', 'sujet')
save(fig, '39-008')
