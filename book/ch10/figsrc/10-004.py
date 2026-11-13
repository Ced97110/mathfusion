import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, x1 = 4, 80
f = lambda v: x0 + v / 500000 * (x1 - x0)
text(ax, 44, 57, r'87 boîtes de 4 316 g', 'encre', 'm')
box(ax, f(0), 22, f(400000) - f(0), 12, 'resultat', label='oui : on charge')
box(ax, f(400000), 22, f(500000) - f(400000), 12, 'limite', label='non')
line(ax, [(f(400000), 18), (f(400000), 38.5)], 'limite', lw=1.4)
text(ax, f(400000), 13, 'limite : 400 000 g', 'limite', 'm')
# three different weights, each named, staggered heights; all give the same answer
for v, h, lab in ((300000, 41, '300 000'), (360000, 47, '360 000'), (375492, 41, '375 492')):
    disc(ax, f(v), 37.5, 1.3, 'sujet')
    if h > 41: line(ax, [(f(v), 38.8), (f(v), h - 2)], 'sujet', lw=0.6, dash=True)
    text(ax, f(v), h, lab, 'sujet', 's')
text(ax, 44, 4, 'Le côté de la limite suffit.', 'resultat', 'm')
save(fig, '10-004')
