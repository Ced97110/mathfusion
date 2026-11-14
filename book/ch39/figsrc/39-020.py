import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

def arc(ax, o, r, d0, d1, role='encre'):
    line(ax, [pt(o, r, d0 + (d1 - d0) * i / 40) for i in range(41)], role)

fig, ax = canvas(46)
u = 0.7                                          # 1 km -> 0.7 mm
line(ax, [(44, 3), (44, 42)], 'fixe', dash=True, lw=0.6)
text(ax, 21, 40, 'polaires : r et θ', 'sujet', 'm')
text(ax, 66, 40, 'cartésiennes : x et y', 'autre', 'm')
# left : polar
OL = (6, 10); PL = pt(OL, 40 * u, 30)
arrow(ax, OL, (40, 10), 'fixe', lw=0.9)
line(ax, [OL, PL], 'sujet', lw=1.8)
arc(ax, OL, 9, 0, 30)
disc(ax, PL[0], PL[1], 1.3, 'sujet'); disc(ax, OL[0], OL[1], 1.1, 'fixe')
text(ax, 15.5, 22, '40 km', 'sujet', 's'); text(ax, 20, 12.6, '30°', 'encre', 's')
text(ax, PL[0] + 2.5, PL[1] + 2.5, 'P')
# right : cartesian
OR = (50, 10); PR = (OR[0] + 34.64 * u, OR[1] + 20 * u); HR = (PR[0], OR[1])
arrow(ax, OR, (84, 10), 'fixe', lw=0.9)
line(ax, [OR, HR], 'varie', lw=1.8)
line(ax, [HR, PR], 'resultat', lw=1.8)
line(ax, [OR, PR], 'fixe', lw=0.8, dash=True)
disc(ax, PR[0], PR[1], 1.3, 'autre'); disc(ax, OR[0], OR[1], 1.1, 'fixe')
text(ax, 62.5, 6, '34,64 km', 'varie', 's')
text(ax, HR[0] + 1.8, 17, '20 km', 'resultat', 's', ha='left')
text(ax, PR[0] + 0.5, PR[1] + 3.2, 'P')
save(fig, '39-020')
