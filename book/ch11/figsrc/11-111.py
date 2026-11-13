import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 6; x0, y0 = 6, 26
b, h = 6, 4
T = (x0 + 2 * s, y0 + h * s)
# left small rectangle: blue lower-right half, grey upper-left half
poly(ax, [(x0, y0), (x0 + 2 * s, y0), T], 'sujet')
poly(ax, [(x0, y0), T, (x0, y0 + h * s)], 'fixe')
# right small rectangle: blue lower-left half, grey upper-right half
poly(ax, [(x0 + 2 * s, y0), (x0 + b * s, y0), T], 'sujet')
poly(ax, [(x0 + b * s, y0), (x0 + b * s, y0 + h * s), T], 'fixe')
line(ax, [(x0, y0), (x0 + b * s, y0), (x0 + b * s, y0 + h * s), (x0, y0 + h * s), (x0, y0)], 'fixe', dash=True)
line(ax, [(x0 + 2 * s, y0), T], 'encre', dash=True, lw=1.0)
text(ax, x0 + 1.3 * s, y0 + 1.0 * s, '4', 'sujet', 's')
text(ax, x0 + 0.7 * s, y0 + 3.0 * s, '4', 'fixe', 's')
text(ax, x0 + 3.5 * s, y0 + 1.0 * s, '8', 'sujet', 's')
text(ax, x0 + 5.0 * s, y0 + 3.0 * s, '8', 'fixe', 's')
text(ax, x0 + b * s / 2, y0 - 4, '$b$ = 6', 'varie', 's')
text(ax, x0 - 3, y0 + h * s / 2, '$h$ = 4', 'varie', 's', rot=90)
box(ax, 50, 40, 34, 9, 'sujet', label='bleu : 4 + 8 = 12', size='s')
box(ax, 50, 27, 34, 9, 'fixe', label='gris : 4 + 8 = 12', size='s')
text(ax, 67, 38, '=', 'resultat', 'l', weight='bold')
text(ax, 44, 13, r'bleu + gris = 24 = $b$ × $h$', 'resultat', 'm')
text(ax, 44, 5, r'triangle = $b$ × $h$ ÷ 2', 'sujet', 'm', weight='bold')
save(fig, '11-111')
