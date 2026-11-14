import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

fig, ax = canvas(46)
text(ax, 44, 41, 'O : le point de départ', 'encre', 'm')
line(ax, [(47, 3), (47, 34)], 'fixe', dash=True, lw=0.6)
# left : radar
OL = (20, 14); A = pt(OL, 20, 30)
arrow(ax, (6, 14), (43, 14), 'fixe', lw=0.9)
line(ax, [OL, A], 'sujet', lw=1.6)
disc(ax, A[0], A[1], 1.4, 'fixe'); disc(ax, OL[0], OL[1], 2, 'sujet')
text(ax, A[0], A[1] + 3.8, 'avion')
text(ax, OL[0], 8, 'O = antenne', 'sujet', 's')
# right : lighthouse
OR = (68, 14); B = (OR[0] - 12, OR[1] + 12)
arrow(ax, (51, 14), (85, 14), 'fixe', lw=0.9)
line(ax, [OR, B], 'sujet', lw=1.6)
disc(ax, B[0], B[1], 1.4, 'fixe'); disc(ax, OR[0], OR[1], 2, 'sujet')
text(ax, B[0], B[1] + 3.8, 'bateau')
text(ax, OR[0], 8, 'O = phare', 'sujet', 's')
save(fig, '39-010')
