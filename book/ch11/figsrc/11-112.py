import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 5; x0, y0 = 6, 14
b, h = 10, 7
T = (x0 + 4 * s, y0 + h * s)
poly(ax, [(x0, y0), (x0 + b * s, y0), T], 'sujet')
line(ax, [(x0, y0), (x0 + b * s, y0), (x0 + b * s, y0 + h * s), (x0, y0 + h * s), (x0, y0)], 'fixe', dash=True)
line(ax, [T, (T[0], y0)], 'varie', lw=1.1, dash=True)
k = 2.0
line(ax, [(T[0], y0 + k), (T[0] + k, y0 + k), (T[0] + k, y0)], 'varie', lw=0.8)
text(ax, x0 + b * s / 2, y0 - 4, '$b$ = 10 m', 'sujet', 's')
text(ax, T[0] - 7.5, y0 + 10, '$h$ = 7 m', 'varie', 's')
text(ax, x0 + 7.5 * s, y0 + 1.5 * s, '35', 'sujet', 'm', weight='bold')
text(ax, 71, 52, 'base : 10', 'sujet', 's')
text(ax, 71, 46, 'hauteur : 7', 'varie', 's')
text(ax, 71, 38, '10 × 7 = 70', 'fixe', 's')
text(ax, 71, 31, '70 ÷ 2 = 35', 'sujet', 's')
text(ax, 71, 22, r'$A$ = 35 m$^2$', 'resultat', 'm', weight='bold')
text(ax, 44, 5, r'$A$ = $b$ × $h$ ÷ 2', 'sujet', 'm')
save(fig, '11-112')
