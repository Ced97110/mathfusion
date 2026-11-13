import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

def arc(ax, o, r, d0, d1, role='encre'):
    line(ax, [pt(o, r, d0 + (d1 - d0) * i / 40) for i in range(41)], role)

fig, ax = canvas(47)
u = 6                                       # 1 km = 6 mm
O = (52, 14); B = (O[0] - 4 * u, O[1] + 4 * u); H = (B[0], O[1])
arrow(ax, (8, 14), (82, 14), 'fixe', lw=0.9)
line(ax, [O, H], 'varie', lw=1.8)
line(ax, [H, B], 'resultat', lw=1.8)
line(ax, [O, B], 'sujet', lw=1.4, dash=True)
arc(ax, O, 8, 0, 134)
arrow(ax, pt(O, 8, 130), pt(O, 8, 135), 'encre', lw=0.8)
disc(ax, O[0], O[1], 1.3, 'sujet'); disc(ax, B[0], B[1], 1.3, 'sujet')
text(ax, 56, 10.5, 'O (phare)', 'encre', 'm', ha='left')
text(ax, B[0], B[1] + 3.5, 'bateau')
text(ax, 40, 10.3, "4 km à l'ouest", 'varie')
text(ax, B[0] - 2.5, 26, '4 km nord', 'resultat', ha='right')
text(ax, 47, 31, 'distance ?', 'sujet', ha='left')
text(ax, 60, 24, 'angle ?')
save(fig, '39-003')
